class Light:
    def turn_on(self):
        print('light turned on')
    def turn_off(self):
        print('light turned off')

class Fan:
    def turn_on(self):
        print('fan turned on')
    def turn_off(self):
        print('fan turned off')

class Switch:
    def __init__(self):
        self.light = Light()
        self.fan = Fan()
    def turn_light_on(self):
            self.light.turn_on()
    def turn_light_off(self):
        self.light.turn_off()
    def turn_fan_on(self):
        self.fan.turn_on()
    def turn_fan_off(self):
        self.fan.turn_off()
    

switch = Switch()
switch.turn_light_on()
switch.turn_light_off()
switch.turn_fan_on()
switch.turn_fan_off()