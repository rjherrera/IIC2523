import asyncio
import os
import pickle

from kademlia.network import Server as KademliaServer
from kademlia_iic2523.ipc import ipcListen
from kademlia_iic2523.storage import MultipleStorage

STATE_FILE = ".state"

class Server(KademliaServer):

    def __init__(self):
        super().__init__(storage=MultipleStorage())

        self.ipcTask = None


    def listen(self, port, ipcCallback):
        super().listen(port)

        if os.path.isfile(STATE_FILE):
            with open(STATE_FILE, "rb") as f:
                data = pickle.load(f)
            self.ksize = data["ksize"]
            self.alpha = data["alpha"]
            self.id = data["id"]
            if len(data["neighbors"]) > 0:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(self.bootstrap(data["neighbors"]))

        self.ipcTask = asyncio.ensure_future(ipcListen(lambda x: ipcCallback(self, x)))

        # Save state every 60 seconds
        super().saveStateRegularly(STATE_FILE, 60)

    def stop(self):
        super().stop()
        if self.ipcTask is not None:
            print(self.ipcTask)
            self.ipcTask.cancel()


