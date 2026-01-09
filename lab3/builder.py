from abc import ABC, abstractmethod

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
    
    def __str__(self):
        parts = []
        if self.cpu:
            parts.append(f"CPU: {self.cpu}")
        if self.ram:
            parts.append(f"RAM: {self.ram}")
        if self.storage:
            parts.append(f"Storage: {self.storage}")
        if self.gpu:
            parts.append(f"GPU: {self.gpu}")
        return " | ".join(parts) if parts else "Пустой компьютер"

class ComputerBuilder(ABC):
    def __init__(self):
        self.computer = Computer()
    
    @abstractmethod
    def add_cpu(self):
        pass
    
    @abstractmethod
    def add_ram(self):
        pass
    
    @abstractmethod
    def add_storage(self):
        pass
    
    @abstractmethod
    def add_gpu(self):
        pass
    
    def get_computer(self):
        return self.computer

class GamingComputerBuilder(ComputerBuilder):
    def add_cpu(self):
        self.computer.cpu = "Intel Core i9"
    
    def add_ram(self):
        self.computer.ram = "32GB DDR5"
    
    def add_storage(self):
        self.computer.storage = "2TB NVMe SSD"
    
    def add_gpu(self):
        self.computer.gpu = "NVIDIA RTX 4090"

class OfficeComputerBuilder(ComputerBuilder):
    def add_cpu(self):
        self.computer.cpu = "Intel Core i5"
    
    def add_ram(self):
        self.computer.ram = "16GB DDR4"
    
    def add_storage(self):
        self.computer.storage = "512GB SSD"
    
    def add_gpu(self):
        self.computer.gpu = "Интегрированная графика"

class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder
    
    def build_computer(self):
        self.builder.add_cpu()
        self.builder.add_ram()
        self.builder.add_storage()
        self.builder.add_gpu()
        return self.builder.get_computer()
    
    def build_basic_computer(self):
        self.builder.add_cpu()
        self.builder.add_ram()
        return self.builder.get_computer()

if __name__ == "__main__":
    print("Строим игровой компьютер:")
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector(gaming_builder)
    gaming_pc = director.build_computer()
    print(gaming_pc)
    
    print("\nСтроим офисный компьютер:")
    office_builder = OfficeComputerBuilder()
    director = ComputerDirector(office_builder)
    office_pc = director.build_computer()
    print(office_pc)
    
    print("\nУпрощённая сборка:")
    office_builder2 = OfficeComputerBuilder()
    director2 = ComputerDirector(office_builder2)
    basic_pc = director2.build_basic_computer()
    print(basic_pc)
