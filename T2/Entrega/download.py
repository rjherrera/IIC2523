from kademlia_iic2523.ipc import ipcSend
import requests
import socket
import sys

FILES_FOLDER = '/user/rjherrera/T2/files'
ERRORS = []

def download(url):
    # we use a try as we may recieve unexpected things. Also to use a friendly way of showing errors if every url fails
    try:
        # we use the requests library to try to download the file
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            # if we can, we dump it to the desired location
            with open('%s/%s' % (FILES_FOLDER, sys.argv[1]), 'wb') as f:
                # in chunks so that it doesn't fail with big files
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            return True
        # we throw an exception if the file wasn't located (if the status code isn't 200)
        raise Exception(r.status_code)
    except Exception as error:
        # we append the errors to a list so that they can be printed only if needed
        ERRORS.append(error)
        return False

def onResponse(message):
    # we get our ip_adress by accessing the socket
    ip_address = socket.gethostbyname(socket.gethostname())
    for url in message:
        # as message is a list of potential places in which the file is located, we iterate over them
        if download(url):
            # we try to download the url and if we succeed, we register ourselves.
            node_url = 'http://%s:11009/%s' % (ip_address, sys.argv[1])
            # 'set' the file in our location (node_url) -> we are now registered as a server for it
            ipcSend('set %s %s' % (sys.argv[1], node_url))
            print('Downloaded %s succesfully and saved into %s/. Serving the file.' % (sys.argv[1], FILES_FOLDER))
            return
    print('File not downloaded. The following errors ocurred:')
    # only if the file wasn't downloaded we print the errors.
    print(*('%d) %s' % (i + 1, ERRORS[i]) for i in range(len(ERRORS))), sep='\n')

# we use the get command and register as a callback the above function
ipcSend('get %s' % sys.argv[1], onResponse)



