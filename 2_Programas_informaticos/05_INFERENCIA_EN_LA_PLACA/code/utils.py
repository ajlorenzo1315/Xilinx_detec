
import os
import time
import threading
import csv

from collections import OrderedDict

import numpy as np

def transform_gt_record(gt_records, class_names):
    '''
    Transform the Ground Truth records of a image to prediction format, in
    order to show & compare in result pic.

    Ground Truth records is a dict with format:
        {'100,120,200,235':'dog', '85,63,156,128':'car', ...}

    Prediction format:
        (boxes, classes, scores)
    '''
    if gt_records is None or len(gt_records) == 0:
        return [], [], []

    gt_boxes = []
    gt_classes = []
    gt_scores = []
    for (coordinate, class_name) in gt_records.items():
        gt_box = [int(x) for x in coordinate.split(',')]
        gt_class = class_names.index(class_name)

        gt_boxes.append(gt_box)
        gt_classes.append(gt_class)
        gt_scores.append(1.0)

    return np.array(gt_boxes), np.array(gt_classes), np.array(gt_scores)

def annotation_parse(annotation_lines, class_names):
    '''
    parse annotation lines to get image dict and ground truth class dict

    image dict would be like:
    annotation_records = {
        '/path/to/000001.jpg': {'100,120,200,235':'dog', '85,63,156,128':'car', ...},
        ...
    }

    ground truth class dict would be like:
    classes_records = {
        'car': [
                ['000001.jpg','100,120,200,235'],
                ['000002.jpg','85,63,156,128'],
                ...
               ],
        ...
    }
    '''
    annotation_records = OrderedDict()
    classes_records = OrderedDict({class_name: [] for class_name in class_names})

    for line in annotation_lines:
        box_records = {}
        image_name = line.split(' ')[0]
        boxes = line.split(' ')[1:]
        for box in boxes:
            #strip box coordinate and class
            class_name = class_names[int(box.split(',')[-1])]
            coordinate = ','.join(box.split(',')[:-1])
            box_records[coordinate] = class_name
            #append or add ground truth class item
            record = [os.path.basename(image_name), coordinate]
            if class_name in classes_records:
                classes_records[class_name].append(record)
            else:
                classes_records[class_name] = list([record])
        annotation_records[image_name] = box_records

    return annotation_records, classes_records


class Sensor():
    def __init__(self, tiempo_muestreo, imprimir_potencia=False, nombre_archivo='power_mesurement.txt',time_max=100):
        self.sensor_midiendo = threading.Event()
        self.imprimir_potencia = imprimir_potencia
        self.tiempo_muestreo = tiempo_muestreo
        self.save = True
        self.data = []
        self.nombre_archivo = nombre_archivo  # Nombre del archivo CSV
        hilo_potencia = threading.Thread(target=self.medicion_energia)
        hilo_potencia.start()
        self.time_max=10000

    def medicion_energia(self):

        ruta = '/sys/class/hwmon'
        nombre_placa = open('/sys/firmware/devicetree/base/model').read().strip()
        
        self.medicion_energia ={"Energia [Wh]":0,"Suma_potencia [W]":0,"Samples":0, "Potencia_media [W]":0,"Intervalo [s]":0}
        dic_sensores = {'ina260_u14': {'region': 'SOM', 'power_rail': 'SOM_5V0'}}
        self.medicion_potencia = {'SOM': 0, 'Total [W]': 0}
        self.medicion_potencia_s = {'SOM': 0, 'Total [W]': 0}
        self.medicion_ampios = {'SOM': 0, 'Total [W]': 0}
        self.medicion_voltios = {'SOM': 0, 'Total [W]': 0}

        carpetas = os.listdir(ruta)
        tiempo_inicio = time.time()
        while True:
            tiempo_fin = time.time()
            if self.time_max< tiempo_fin - tiempo_inicio:
                print(tiempo_fin - tiempo_inicio)
                self.detener()
            for region_potencia in self.medicion_potencia:
                self.medicion_potencia[region_potencia] = 0

            for carpeta in carpetas:
                ruta_subcarpeta = os.path.join(ruta, carpeta)
                archivos = os.listdir(ruta_subcarpeta)

                if 'name' in archivos:
                    with open(os.path.join(ruta_subcarpeta, 'name')) as archivo_nombre_sensor:
                        nombre_sensor = archivo_nombre_sensor.read().strip()
                    

                    if 'ina' in nombre_sensor:
                        
                        with open(os.path.join(ruta_subcarpeta, 'in1_input')) as archivo_voltaje_sensor:
                            voltaje_sensor = archivo_voltaje_sensor.read().strip() #mV

                        with open(os.path.join(ruta_subcarpeta, 'curr1_input')) as archivo_corriente_sensor:
                            corriente_sensor = archivo_corriente_sensor.read().strip() #mA

                        with open(os.path.join(ruta_subcarpeta, 'power1_input')) as archivo_potencia_sensor:
                            potencia_sensor = archivo_potencia_sensor.read().strip() #mW

                        dic_sensores[nombre_sensor].update({'voltaje_bus': voltaje_sensor,
                                                            'corriente_shunt': corriente_sensor,
                                                            'potencia': potencia_sensor})

            if self.sensor_midiendo.is_set():
                tiempo_fin = time.time()
                tiempo_total = tiempo_fin - tiempo_inicio
                self.medicion_energia = {
                    "Intervalo [s]": round(tiempo_total, 4),
                    "Potencia_media [W]": round(self.medicion_energia["Suma_potencia [W]"] / self.medicion_energia["Samples"], 4),
                    "Energia [Wh]": round(self.medicion_energia["Suma_potencia [W]"] * (tiempo_total / self.medicion_energia["Samples"]) * (1 / 3600), 4),  # vatios hora
                    "Suma_potencia [W]": round(self.medicion_energia["Suma_potencia [W]"], 4),
                    "Samples": self.medicion_energia["Samples"]
                }
                
                
                #break
            
            for sensor in dic_sensores:

                self.medicion_potencia[dic_sensores[sensor]['region']] = (float(dic_sensores[sensor]['voltaje_bus']) *
                                                                    float(dic_sensores[sensor]['corriente_shunt']) / 1000000)
                
                self.medicion_potencia_s[dic_sensores[sensor]['region']] = (float(dic_sensores[sensor]['potencia']) / 1000000)

                self.medicion_ampios[dic_sensores[sensor]['region']] = (float(dic_sensores[sensor]['corriente_shunt']) / 1000)

                self.medicion_voltios[dic_sensores[sensor]['region']] = (float(dic_sensores[sensor]['voltaje_bus'])  / 1000)

            self.medicion_potencia['Total [W]'] = sum(self.medicion_potencia.values()) -self. medicion_potencia['Total [W]']

            self.medicion_energia["Suma_potencia [W]"] += self.medicion_potencia['Total [W]']
            self.medicion_energia["Samples"] += 1

            if self.imprimir_potencia:
                print(tiempo_fin - tiempo_inicio)
                print("Nombre de la placa:", nombre_placa)
                print("Nombre del sensor:", nombre_sensor)
                print({clave: round(valor, 4) for clave, valor in self.medicion_potencia.items()})
                print({clave: round(valor, 4) for clave, valor in self.medicion_ampios.items()})
                print({clave: round(valor, 4) for clave, valor in self.medicion_voltios.items()})
                print({clave: round(valor, 4) for clave, valor in self.medicion_potencia_s.items()})
                self.guardar_datos_csv()
            if self.save:
                # Almacenar los datos en la lista 'data' en cada iteración
                self.data.append({'tiempo': float(tiempo_fin - tiempo_inicio),
                    'Potencia[W]': list(self.medicion_potencia.values())[0],
                    'Potencia S [W]': list(self.medicion_potencia_s.values())[0],
                    'Amperios[A]': list(self.medicion_ampios.values())[0],
                    'Voltios[V]': list(self.medicion_voltios.values())[0]
                })
                self.guardar_datos_csv()
            #self.sensor_midiendo.set()
            time.sleep(self.tiempo_muestreo)

    def guardar_datos_csv(self):
        # Guardar los datos en el archivo CSV
        with open(self.nombre_archivo, 'w', newline='') as archivo_csv:
            campos = ['tiempo','Potencia[W]','Potencia S [W]', 'Amperios[A]', 'Voltios[V]']  # Definir los campos del CSV

            writer = csv.DictWriter(archivo_csv, fieldnames=campos)

            # Escribir la línea de encabezado
            writer.writeheader()

            # Escribir los datos en cada línea
            for dato in self.data:
                writer.writerow(dato)

    def detener(self):
        self.sensor_midiendo.set()
        self.guardar_datos_csv()  

if __name__=='__main__':
   
    medidor=Sensor(0.01, False,'power_drain_t.txt',10)
    time.sleep(5)
    medidor.detener()
