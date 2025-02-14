from abc import ABC, abstractmethod


class Burger(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.name=""

    def getName(self) -> str:
        return self.name
    
    @abstractmethod
    def addToppings(self,topings:list):
        pass

class CheeseBurger(Burger):
    def __init__(self) -> None:
        super().__init__()
        self.name="CheeseBurger"

    def getName(self) -> str:
        return super().getName()
    
    def addToppings(self,topings):
        self.topings = topings

class BurgerFactory(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def createBurger(burgerType:str,topings):
        pass

    
class CheeseBurgerFactory(BurgerFactory):
    def __init__(self) -> None:
        super().__init__()

    
    def createBurger(self,burgerType: str,topings):
        if burgerType=="cheese":
            cheese = CheeseBurger()
            cheese.addToppings(topings)
            return cheese
        

cheeseFactory = CheeseBurgerFactory()

burger = cheeseFactory.createBurger("cheese",["cheese","mayo","bacon"])

print(burger.topings)