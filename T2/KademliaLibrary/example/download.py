from kademlia_iic2523.ipc import ipcSend
import requests
import socket
import sys

FILES_FOLDER = '/user/rjherrera/T2/files'

def download(url):
    # try as we may recieve unexpected things. Also to use a friendly way of showing errors
    try:
        # use the requests library to try to download the file
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            # if we can we dump it to the desired location
            with open('%s/%s' % (FILES_FOLDER, sys.argv[1]), 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            return True
        raise Exception(r.status_code)
    except Exception as error:
        print(error)
        return False

def onResponse(message):
    ip_address = socket.gethostbyname(socket.gethostname())
    for url in message:
        if download(url):
            node_url = 'http://%s:11009/%s' % (ip_address, sys.argv[1])
            # 'set' the file in our location (node_url) -> we are now registered as a server for it
            ipcSend('set %s %s' % (sys.argv[1], node_url))
            return
    print('File not downloaded.')

ipcSend('get %s' % sys.argv[1], onResponse)



