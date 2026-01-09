from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self, cargo):
        pass

class Truck(Transport):
    def deliver(self, cargo):
        return f"🚚 Грузовик доставляет '{cargo}' по дороге"

class Ship(Transport):
    def deliver(self, cargo):
        return f"🚢 Корабль доставляет '{cargo}' по морю"

class Plane(Transport):
    def deliver(self, cargo):
        return f"✈️ Самолёт доставляет '{cargo}' по воздуху"

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass
    
    def plan_delivery(self, cargo):
        transport = self.create_transport()
        result = transport.deliver(cargo)
        print(result)
        return result

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Plane()

if __name__ == "__main__":
    cargo = "компьютеры"
    
    print("Доставка по дороге:")
    RoadLogistics().plan_delivery(cargo)
    
    print("\nДоставка морем:")
    SeaLogistics().plan_delivery(cargo)
    
    print("\nДоставка воздухом:")
    AirLogistics().plan_delivery(cargo)
