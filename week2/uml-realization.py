from abc import *
class Printable(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def newPage(self):
        pass

class PrintClass(Printable):
    def show(self):
        print("show implemented")

    def newPage(self):
        print("newPage implemented")

pc = PrintClass()
pc.show()

'''
출력 결과
show implemented
'''