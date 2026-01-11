# chain.py
class Handler:
    def __init__(self):
        self.next = None
    
    def set_next(self, handler):
        self.next = handler
        return handler
    
    def handle(self, request):
        if self.next:
            return self.next.handle(request)
        return None

class Manager(Handler):
    def handle(self, request):
        if request <= 1000:
            return f"Менеджер одобрил запрос на {request} руб."
        return super().handle(request)

class Director(Handler):
    def handle(self, request):
        if request <= 5000:
            return f"Директор одобрил запрос на {request} руб."
        return super().handle(request)

class CEO(Handler):
    def handle(self, request):
        return f"Генеральный директор одобрил запрос на {request} руб."

# Пример
if __name__ == "__main__":
    manager = Manager()
    director = Director()
    ceo = CEO()
    
    manager.set_next(director).set_next(ceo)
    
    print(manager.handle(500))
    print(manager.handle(3000))
    print(manager.handle(10000))
