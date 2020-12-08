class Burger:
    def __init__(self, burger_type, drink, side):
        self.burger_type = burger_type
        self.drink = drink
        self.side = side
        self.toppings = []
        
    def add_toppings(self, *topping):
        self.toppings.append(topping)

    def get_toppings(self):
        print(f'You added the following toppings: ')
        for topping in self.toppings:
            print(f'{topping}')

    def summary(self):
        print(f'You want a {self.burger_type} burger, a {self.drink}, side of {self.side}, and {self.toppings} on your burger.')