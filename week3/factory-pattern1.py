# 차량 인터페이스
class Vehicle:
    def drive(self):
        pass

# 구체적인 차량 클래스
class Car(Vehicle):
    def drive(self):
        return "Car driving."

class Truck(Vehicle):
    def drive(self):
        return "Truck driving."

class Motorcycle(Vehicle):
    def drive(self):
        return "Motorcycle zooming."

# 팩토리 인터페이스
class VehicleFactory:
    def create_vehicle(self):
        pass

# 구체적인 팩토리 클래스
class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()

class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Motorcycle()

# 사용 예
def client_code(factory: VehicleFactory):
    vehicle = factory.create_vehicle()
    print(vehicle.drive())

car_factory = CarFactory()
client_code(car_factory)  # Car driving.

truck_factory = TruckFactory()
client_code(truck_factory)  # Truck driving.

motorcycle_factory = MotorcycleFactory()
client_code(motorcycle_factory)  # Motorcycle zooming.
