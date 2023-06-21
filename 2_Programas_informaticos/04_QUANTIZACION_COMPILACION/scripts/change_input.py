import tensorflow as tf

# Ruta del modelo pb existente
ruta_modelo_pb = '../tf_model/yolov4-mod-xilinx.pb'
# Ruta de salida para el modelo modificado
ruta_modelo_modificado_pb = '../tf_model/yolov4-mod-xilinx_512_512.pb'

# Cargar el modelo pb existente
with tf.io.gfile.GFile(ruta_modelo_pb, 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())

# Modificar el tamaño de entrada del modelo
for node in graph_def.node:
    if 'input' in node.name:
        node.attr['shape'].shape.dim[1].size = 512  # Ancho
        node.attr['shape'].shape.dim[2].size = 512  # Alto
        node.attr['shape'].shape.dim[3].size = 3    # Canales

# Guardar el nuevo modelo modificado
with tf.compat.v1.Graph().as_default() as graph:
    tf.import_graph_def(graph_def, name='')
    tf.io.write_graph(graph_def, './', ruta_modelo_modificado_pb, as_text=False)

print("Modelo modificado guardado en", ruta_modelo_modificado_pb)
