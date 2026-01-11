from strategy import ShoppingCart, CreditCardPayment, PayPalPayment
from chain import Manager, Director, CEO
from iterator import BookCollection
from proxy import DatabaseProxy
from bridge import TV, Radio, BasicRemote, AdvancedRemote
from adapter import EuropeanSocket, AmericanSocket, SocketAdapter

def demo_all():
    print("="*50)
    print("ЛАБОРАТОРНАЯ 4: ПОВЕДЕНЧЕСКИЕ И СТРУКТУРНЫЕ ПАТТЕРНЫ")
    print("="*50)
    
    print("\n1. СТРАТЕГИЯ:")
    cart = ShoppingCart()
    cart.set_strategy(CreditCardPayment())
    print(cart.checkout(1000))
    cart.set_strategy(PayPalPayment())
    print(cart.checkout(500))
    
    print("\n2. ЦЕПОЧКА ОБЯЗАННОСТЕЙ:")
    manager = Manager()
    director = Director()
    ceo = CEO()
    manager.set_next(director).set_next(ceo)
    print(manager.handle(500))
    print(manager.handle(3000))
    
    print("\n3. ИТЕРАТОР:")
    library = BookCollection()
    library.add_book("Книга 1")
    library.add_book("Книга 2")
    for book in library:
        print(f"  {book}")
    
    print("\n4. ПРОКСИ:")
    proxy = DatabaseProxy()
    proxy.authenticate("secret123")
    print(proxy.get_data())
    
    print("\n5. МОСТ:")
    tv = TV()
    remote = AdvancedRemote(tv)
    print(remote.power())
    
    print("\n6. АДАПТЕР:")
    american = AmericanSocket()
    adapter = SocketAdapter(american)
    print(adapter.plug())

if __name__ == "__main__":
    demo_all()
