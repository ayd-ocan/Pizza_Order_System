from pizza import *

#Decorator
class Decorator(pizza):
    def __init__(self, Pizza):
        #Use Pizza functions in init function.
        self.get_cost()
        self.get_description()
        self.component = Pizza
    def get_cost(self):
        return pizza.get_cost(self)
    def get_description(self):
        return pizza.get_description(self)

#Sub Sauce Classes which are childs of Decorator.
class Olives(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
    cost = 1
    description = "Olives"

class Mushrooms(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
    cost = 2
    description = "Mushrooms"

class GoatCheese(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
    cost = 3
    description = "GoatCheese"

class Meat(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
    cost = 4
    description = "Meat"

class Onions(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
    cost = 5
    description = "Onions"

class Corn(Decorator):
    def __init__(self,Pizza):
        super().__init__(Pizza)
    cost = 6
    description = "Corn"
