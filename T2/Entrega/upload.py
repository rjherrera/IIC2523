from kademlia_iic2523.ipc import ipcSend
from shutil import copyfile
import socket
import sys
import os

FILES_FOLDER = '/user/rjherrera/T2/files'

# setting variables (file_name to publish, ip of the host, (i.e. us) to get the url, url to publish)
file_name = os.path.basename(sys.argv[1])
ip_address = socket.gethostbyname(socket.gethostname())
url = 'http://%s:11009/%s' % (ip_address, file_name)

# 'copy' the file into the serving location -> we are now serving it as we have a running server on that location
copyfile(sys.argv[1], '%s/%s' % (FILES_FOLDER, file_name))
# 'set' the file in our location (url) -> we are now registered in the DHT as a server for it
ipcSend('set %s %s' % (file_name, url))
print('Uploaded %s succesfully.' % file_name)
