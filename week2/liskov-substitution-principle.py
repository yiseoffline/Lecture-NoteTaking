class Vehicle:
    def start_engine(self):
        if self.has_fuel():
            print('엔진이 시작됩니다')
        else:
            print('연료가 부족합니다')
    def has_fuel(self):
        return True

class Car(Vehicle):
    def has_fuel(self):
        return True
    
class ElectricCar(Vehicle):
    def has_fuel(self):
        return True

class ElectricCarNoLSP(Vehicle):
    def has_fuel(self):
        return NotImplementedError('이 차량은 전기차이므로 연료 체크를 수행할 수 없습니다')

def attempt_to_start_engine(vehicle):
    vehicle.start_engine()

car=Car()
electric_car = ElectricCar()
electric_car_nolsp = ElectricCarNoLSP()

print('LSP를 따르는 경우 : ')
attempt_to_start_engine(car)
attempt_to_start_engine(electric_car)

print('\nLSP를 따르지 않는 경우 : ')
try:
    attempt_to_start_engine(electric_car_nolsp)
except NotImplementedError as e:
    print(f"오류 : {e}")