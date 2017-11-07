from kademlia_iic2523.ipc import ipcSend
import sys

# Callback que se ejecutará con la respuesta del nodo
def onResponse(message):
    print(message)

# Envía el comando "get key" al nodo
ipcSend("get " + sys.argv[1], onResponse)

