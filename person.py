class Person:
    def __init__(self, name, age, favorite_color):
        self.name = name
        self.age = age
        self.color = favorite_color
    
    def introduce(self):
        print(f'Hi, my name is {self.name} and I am {self.age} years old.')

    def fav_color(self):
        print(f'My favorite color is {self.color}.')

# omar = Person('Omar', 19, 'Red')
# omar.introduce()
# omar.fav_color()