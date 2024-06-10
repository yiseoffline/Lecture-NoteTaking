import time
from abc import *

class Printable(metaclass=ABCMeta):

    def __init__(self):
        self.name = ""

    @abstractmethod
    def setPrinterName(self, name):
        pass

    @abstractmethod
    def getPrinterName(self):
        pass

    @abstractmethod
    def printText(self, msg):
        pass

class Printer(Printable):

    def __init__(self, name):
        self.name = name
        self.heavyJob("Printer의 인스턴스("+self.name+")을 생성 중")

    def setPrinterName(self, name):
        self.name = name

    def getPrinterName(self):
        return self.name

    def printText(self, msg):
        print("===" + self.name + "===", end=": ")
        print(msg)

    def heavyJob(self, msg):
        print(msg)
        for i in range(5):
            time.sleep(1)
        print("완료")

class PrinterProxy(Printable):

    def __init__(self, name):
        self.name = name
        self.real = None

    def realize(self):
        if self.real is None:
            self.real = Printer(self.name)

    def setPrinterName(self, name):
        if self.real is not None:
            self.real.setPrinterName(name)
        self.name = name

    def getPrinterName(self):
        return self.name

    def printText(self, msg):
        self.realize()
        self.real.printText(msg)


p = PrinterProxy("보스톤")
print("현재 이름은 " + p.getPrinterName() + "입니다.")
p.setPrinterName("머큐리")
print("현재 이름은 " + p.getPrinterName() + "입니다.")
p.printText("hello, How are you?")
p.printText("Do you hear me?")

p.setPrinterName("아폴로")
print("현재 이름은 " + p.getPrinterName() + "입니다.")
p.printText("We successfully arrived the moon.")
