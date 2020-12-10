class User:
    def __init__(self, name, age):
        # all attributes are public.
        self.name = name
        self.age = age

    # greets the user.
    def greet_user(self):
        print(f'Hi, {self.name}! I will assist you in finding songs.')
    
    # displays the user's name and age.
    def user_age(self):
        print(f'{self.name} is {self.age} years old.')

omar = User('Omar Lopez', 19)
omar.greet_user()
omar.user_age()