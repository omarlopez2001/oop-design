class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet_user(self):
        print(f'Hi, {self.name}! I will assist you in finding songs.')
    
    def user_age(self):
        print(f'{self.name} is {self.age} years old.')

# omar = User('Omar Lopez', 18)
# omar.greet_user()
# omar.user_age()