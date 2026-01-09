from singleton import Singleton, DatabaseConnection
from factory_method import RoadLogistics, SeaLogistics, AirLogistics
from abstract_factory import WindowsFactory, MacFactory, Application
from builder import GamingComputerBuilder, OfficeComputerBuilder, ComputerDirector

def demo_all_patterns():
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ ВСЕХ ПОРОЖДАЮЩИХ ПАТТЕРНОВ")
    print("=" * 50)
    
    print("\n1. SINGLETON (Одиночка):")
    s1 = Singleton()
    s2 = Singleton()
    print(f"   s1 is s2: {s1 is s2}")
    s1.show()
    
    print("\n2. FACTORY METHOD (Фабричный метод):")
    logistics = [RoadLogistics(), SeaLogistics(), AirLogistics()]
    for log in logistics:
        log.plan_delivery("ноутбуки")
    
    print("\n3. ABSTRACT FACTORY (Абстрактная фабрика):")
    factory = WindowsFactory()
    app = Application(factory)
    app.create_ui()
    app.render()
    
    print("\n4. BUILDER (Строитель):")
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)
    gaming_pc = director.build_computer()
    print(f"   Игровой ПК: {gaming_pc}")
    
    office_builder = OfficeComputerBuilder()
    director.builder = office_builder
    office_pc = director.build_computer()
    print(f"   Офисный ПК: {office_pc}")

if __name__ == "__main__":
    demo_all_patterns()
