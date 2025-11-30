class Car:
    def __init__(self, name, price, mph, hp):
        self.name = name
        self.price = price
        self.mph = mph
        self.hp = hp
    
    def start(self):
        print("breemmmmemem emmememmmmmmbrmbnmnm (starting car)")
    def stats(self):
        print(f"{self.name}, ${self.price}, {self.mph}mph, {self.hp}hp")

corolla = Car("Toyota Corolla", 15200, 190, 150)
corolla.start()
corolla.stats()