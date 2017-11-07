from kademlia_iic2523.ipc import ipcSend
import sys

# Envía el string "set key value" al nodo
ipcSend("set " + sys.argv[1] + " " + sys.argv[2])
