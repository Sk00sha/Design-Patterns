class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Car()
    # Write your code here

class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Bike()
    # Write your code here

class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Truck()
    # Write your code here
