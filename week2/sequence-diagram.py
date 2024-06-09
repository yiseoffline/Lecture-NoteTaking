class Device():
    def write(self):
        print('write')

class Server():
    def __init__(self):
        self.device = Device()
    def open(self):
        pass
    def print(self):
        self.device.write()
    def close(self):
        pass

class Client():
    def __init__(self):
        self.server = Server()
    def work(self):
        self.server.open()
        self.server.print()
        self.server.close()

c = Client()
c.work()