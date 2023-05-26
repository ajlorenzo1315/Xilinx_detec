# CUDa

<pre>

 WARNING: Unable to determine the path to install the libglvnd EGL vendor     
           library config files. Check that you have pkg-config and the        
           libglvnd development libraries installed, or specify a path with    
           --glvnd-egl-config-path.

</pre>


# Docker

Error de permisos docker 
<pre>
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/version": dial unix /var/run/docker.sock: connect: permission denied
</pre>
solución
<pre>
sudo chmod 666 /var/run/docker.sock
</pre>
