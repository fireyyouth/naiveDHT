import pickle
import hashlib
from xmlrpc.client import ServerProxy
class DHT:
    def __init__(self, nodes):
        self.proxies = [x for x in map(ServerProxy, nodes)]
    def nodeId(self, key):
        sha1 = hashlib.sha1()
        sha1.update(pickle.dumps(key))
        return int.from_bytes(sha1.digest(), 'little') % len(self.proxies)
    def get(self, key):
        return self.proxies[self.nodeId(key)].get(key)
    def put(self, pair):
        self.proxies[self.nodeId(pair[0])].put((pair[0], pair[1]))

