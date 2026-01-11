class EuropeanSocket:
    def voltage(self):
        return 220
    
    def plug(self):
        return "Европейская вилка"

class AmericanSocket:
    def voltage(self):
        return 110
    
    def plug(self):
        return "Американская вилка"

class SocketAdapter:
    def __init__(self, socket):
        self.socket = socket
    
    def voltage(self):
        return self.socket.voltage()
    
    def plug(self):
        original = self.socket.plug()
        return f"Адаптер: {original} → Европейская вилка"

if __name__ == "__main__":
    european = EuropeanSocket()
    print(f"Евророзетка: {european.voltage()}V, {european.plug()}")
    
    american = AmericanSocket()
    adapter = SocketAdapter(american)
    print(f"Через адаптер: {adapter.voltage()}V, {adapter.plug()}")
