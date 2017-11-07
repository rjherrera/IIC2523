# kademlia-iic2523

Wrapper de [bmuller/kademlia](http://github.com/bmuller/kademlia) que permite múltiples valores por llave y acepta comandos a través de sockets unix. Creada para que los alumnos la usen en la tarea 2 del ramo iic2523 - Sistemas Distribuidos.

Si encuentran algún error manden PRs porfa! 

PD: tuve que modificar un poco la librería de kademlia para aceptar múltiples valores por llaves, los cambios están en [vdrg/kademlia](http://github.com/vdrg/kademlia), en la branch "iic2523".


## Ejemplos

* [server.py](./example/server): este nodo va a estar corriendo en el cluster. Lo subí por si quieren probarlo localmente.
* [node.py](./example/node.py): este nodo procesa los comandos recibidos e interactúa con la DHT. Recibe como argumento el puerto a escuchar. Debe estar corriendo antes de ejecutar `set.py`/`get.py`.
* [get.py](./example/get.py): recibe como argumento la llave que quieren buscar en la DHT.
* [set.py](./example/set.py): recibe como argumento una llave y un valor para setear en la DHT.

## Instrucciones

Ustedes deben crear los programas `upload.py` y `download.py` (partan modificando `set.py` y `get.py`):

* `upload.py`: recibe como argumento el path de un archivo y comienza a servirlo. Además debe interactuar con su nodo de kademlia y setear el valor `http://URL-PARA-DESCARGAR-EL-ARCHIVO` para la llave `NOMBRE-DEL-ARCHIVO`. Pueden servir el archivo como quieran: una forma fácil de hacerlo es simplemente copiando el archivo en un directorio `uploads` y servir ese directorio completo.

* `download.py`: recibe como argumento el nombre de un archivo, interactúa con su nodo de kademlia para obtener las URLs donde está siendo servido el archivo, y luego lo descarga. Da lo mismo la URL de donde lo descargan, pero si una no funciona (su compañero dejó de servir el archivo) deben probar con las demás. Además, una vez que se descargue el archivo, deben empezar a servirlo ustedes mismos (y setear en la DHT la nueva url donde está siendo servido).

## Instalación

Esta librería estará instalada en el cluster, por lo que simplemente deben importarla. Si quieren probar localmente, pueden instalarla con:

```
$ pip install git+https://github.com/bmuller/rpcudp@python3.5
$ pip install git+https://github.com/vdrg/kademlia@IIC2523
$ pip install git+https://github.com/vdrg/kademlia-iic2523
```
