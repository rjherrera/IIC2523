import logging
import asyncio

from kademlia.network import Server
from kademlia_iic2523.storage import MultipleStorage
logging.basicConfig(level=logging.DEBUG)
loop = asyncio.get_event_loop()
loop.set_debug(True)
PORT = 8468

server = Server(storage=MultipleStorage())
server.listen(PORT)

print("Listening at port", PORT)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.stop()
loop.close()
