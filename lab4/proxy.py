class RealDatabase:
    def get_data(self):
        return "Важные данные из базы"

class DatabaseProxy:
    def __init__(self):
        self.real_db = None
        self.access = False
    
    def authenticate(self, password):
        if password == "secret123":
            self.access = True
            return True
        return False
    
    def get_data(self):
        if not self.access:
            return "Доступ запрещен"
        if not self.real_db:
            self.real_db = RealDatabase()
        return self.real_db.get_data()

if __name__ == "__main__":
    proxy = DatabaseProxy()
    print(proxy.get_data())
    
    proxy.authenticate("wrong")
    print(proxy.get_data())
    
    proxy.authenticate("secret123")
    print(proxy.get_data())
