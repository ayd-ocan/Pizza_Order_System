#Super Class
class pizza:
    def get_description(self):
        return self.description
    def get_cost(self):
        return self.cost
#SubClasses
class Classic(pizza):
    description = "Classic Pizza"
    cost = 5

class Margherita(pizza):
    description = "Margherita Pizza"
    cost = 10

class TurkPizza(pizza):
    description = "Turk Pizza"
    cost = 20

class PlainPizza(pizza):
    description = "Plain Pizza"
    cost = 25