class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = "Я единственный экземпляр!"
        return cls._instance
    
    def show(self):
        print(f"Singleton говорит: {self.value}")

def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = "Подключение установлено"
        print("Создано подключение к БД")
    
    def query(self, sql):
        return f"Выполняем запрос: {sql}"

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(f"s1 is s2: {s1 is s2}")
    s1.show()
