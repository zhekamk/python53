# завдання:
# Вам потрібно розробити програму для управління замовленнями в онлайн-магазині. У програмі повинна бути можливість:
#
# Створювати замовлення.
# Розраховувати загальну вартість замовлення з урахуванням знижок.
# Генерувати рахунок-фактуру для замовлення.
# Зберігати інформацію про замовлення.
# Ваша задача — реалізувати цю програму, використовуючи принципи SOLID, щоб забезпечити гнучкість, розширюваність і підтримуваність коду.


from abc import ABC, abstractmethod

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, price):
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, price):
        return price


class TenPercentDiscount(DiscountStrategy):
    def apply(self, price):
        return price * 0.9


class Order:
    def __init__(self, items, discount_strategy):
        self.items = items
        self.discount_strategy = discount_strategy

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return self.discount_strategy.apply(total)



class InvoiceGenerator:
    def generate(self, order):
        total = order.calculate_total()
        print("--- РАХУНОК-ФАКТУРА ---")
        for item in order.items:
            print(f"{item.name}: {item.price} грн")
        print(f"Разом (зі знижкою): {total:.2f} грн")



class OrderRepository(ABC):
    @abstractmethod
    def save(self, order):
        pass


class FileOrderRepository(OrderRepository):
    def save(self, order):
        print("Замовлення успішно збережено у файл.")



if __name__ == "__main__":
    items = [Item("Ноутбук", 30000), Item("Мишка", 500)]
    discount = TenPercentDiscount()
    order = Order(items, discount)
    invoice = InvoiceGenerator()
    invoice.generate(order)
    repo = FileOrderRepository()
    repo.save(order)