# strategy.py
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплачено {amount} руб. кредитной картой"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплачено {amount} руб. через PayPal"

class ShoppingCart:
    def __init__(self):
        self.strategy = None
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def checkout(self, amount):
        if self.strategy:
            return self.strategy.pay(amount)
        return "Не выбран способ оплаты"

# Пример
if __name__ == "__main__":
    cart = ShoppingCart()
    
    cart.set_strategy(CreditCardPayment())
    print(cart.checkout(1000))
    
    cart.set_strategy(PayPalPayment())
    print(cart.checkout(500))
