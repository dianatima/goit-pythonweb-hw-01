from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


class Vehicle(ABC):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {self.region}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {self.region}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, "EU Spec")


# Використання
if __name__ == "__main__":
    # US factory
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Toyota", "Corolla")
    us_car.start_engine()
    us_moto = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_moto.start_engine()

    # EU factory
    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("Toyota", "Corolla")
    eu_car.start_engine()
    eu_moto = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    eu_moto.start_engine()
