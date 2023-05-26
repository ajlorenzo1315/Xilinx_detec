#ESTES PASOS DEBENSE INSTALAR MANUALMENTE SE QUERES QUE A TÚA TARXETA NVIDA SEXA EMPREGADA
#COMO UN DISPOSITIVO DE CALCULO. O FORMATO DE SCRIPT DE SHELL SO É PARA SECUENCIAR O ORDE DOS PASOS
# POR EXEMPLO, AS LIBCUDA DEBES IDENTIFICARTE NA WEB DE NVIDIA PARA OBTER AS TÚAS LIGAZÓNS DE DESCARGA.

# 1. ACTUALIZAMOS UBUNTU

sudo apt-get -y update
sudo apt-get -y upgrade         # descomenta para actualizar os paquetes instalados
# sudo apt-get -y dist-upgrade  # descomenta para soportar cambios nas versions dos paquetes
sudo apt-get -y autoremove    # descomenta para eliminar os paquetes que xa nos son precisos



# 1.-INSTALA O ULTIMO DRIVER DE NVIDIA PARA A TÚA TARXETA.
# Precisas desinstalar o driver antiguo; sudo apt purge nvidia-driver-XXX 

version_driver='530'

sudo apt install nvidia-driver-$version_driver


#INSTALAMOS CUDA TOOLKIT
# Vai a esta dirección e selecciona as opcións en función da túa maquina, tarxeta e SO.
# CUDA: https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=2004&target_type=deblocal
# Unha vez rematada a elección, darache unha serie de comando (como os que están abaixo) que debes executar dende a túa consola.

wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda-repo-ubuntu2204-11-7-local_11.7.0-515.43.04-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-11-7-local_11.7.0-515.43.04-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-11-7-local/cuda-*-keyring.gpg /usr/share/keyrings/sudo apt-get updatesudo apt-get -y install cuda


# Install libcudnn: https://developer.nvidia.com/Cudnn
# Par obter esta ligazón tes que identificarte na web de NVIDIA e selccionar os paquetes de:
# libcudnnX.*, libcudnnX-dev* e, se queres,o llibcudnnX-samples*.
# Unha vez os decarges, executa as ordes de sudo apt-get install ...

#wget https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.9.0/11.7_20201106/Ubuntu22_04-x64/libcudnn8_8.9.0.131_1.0-1_amd64.deb
#wget https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.0.5/11.1_20201106/Ubuntu20_04-x64/libcudnn8-dev_8.0.5.39-1+cuda11.1_amd64.deb
#wget https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.0.5/11.1_20201106/Ubuntu20_04-x64/libcudnn8-samples_8.0.5.39-1+cuda11.1_amd64.deb
#instalamos os paquetes de cuDNN
sudo apt-get install -y cudnn-local-repo-ubuntu2204-8.9.0.131_1.0-1_amd64.deb
#sudo apt-get install -y libcudnn8-dev_8.0.5.39-1+cuda11.1_amd64.deb
#sudo apt-get install -y llibcudnn8-samples_8.0.5.39-1+cuda11.1_amd64.deb

#SE TODO FOI BEN, SO NOS QUEDA MODIFICAR O NOSO FICHEIRO DE CONFIGURACIÓN DA BASH PARA QUE
# OS PATH DO NOSO USUARIO ATOPEN ONDE ESTÁ INSTALADO CUDA. 
# OLLO: DEBES ADAPTAR OS PATH A VERSION DE CUDA QUE INSTALES!! NESTE CASO E A CUDA11.1
#Modificamos o ficheiro ~/.bashrc
echo "#Cambiamos os pahts pola instalacion de cuda" >> ~/.bashrc
echo "export PATH=/usr/local/cuda-11.1/bin:$PATH" >> ~/.bashrc
echo "export LD_LIBRARY_PATH=/usr/local/cuda-11.1/lib64:$LD_LIBRARY_PATH" >> ~/.bashrc
echo "export CUDA_HOME=/usr/local/cuda-11.1" >> ~/.bashrc

