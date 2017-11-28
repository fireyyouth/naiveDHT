#run this script followed by ip port
from sys import argv
from xmlrpc.server import SimpleXMLRPCServer
class Map:
     def __init__(self):
             self.dict = {}
     def get(self, key):
        ret = self.dict.get(key) 
        if ret == None:
            ret = False
        return ret
     def put(self, pair):
        self.dict[pair[0]] = pair[1]
        return pair
if len(argv) == 3:
    server = SimpleXMLRPCServer((argv[1], int(argv[2])))
    server.register_instance(Map())
    server.serve_forever()
else:
    print('run this script followed by ip port')
