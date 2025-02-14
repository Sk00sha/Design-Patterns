class Burger:
    def __init__(self) -> None:
        self.meat = ""
        self.toppings = []
        
    def __str__(self):
        return f"{self.toppings} meat {self.meat} "

    def set_topings(self,topings):
        self.toppings = topings
    
    def set_meat(self,meat):
        self.meat = meat
    
class BurgerBuilder:
    def __init__(self) -> None:
        self.burger = Burger()

    def add_meat(self,meat):
        self.burger.set_meat(meat)
        return self

    def add_toppings(self,topings):
        self.burger.set_topings(topings)
        return self

    def build(self):
        return self.burger


burger = BurgerBuilder()
burger.add_meat("meat").add_toppings(["lettuce"]).build()
print(burger)