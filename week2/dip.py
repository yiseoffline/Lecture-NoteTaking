from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class Light(Switchable):
    def turn_on(self):
        print('light turned on')
    def turn_off(self):
        print('light turned off')

class Fan(Switchable):
    def turn_on(self):
        print('fan turned on')
    def turn_off(self):
        print('fan turned off')

class Switch:
    def __init__(self, device):
        self.device = device
    def turn_on(self):
        self.device.turn_on()
    def turn_off(self):
        self.device.turn_off()

light = Light()
fan = Fan()

switch1 = Switch(light)
switch1.turn_on()
switch1.turn_off()

switch2 = Switch(fan)
switch2.turn_on()
switch2.turn_off()