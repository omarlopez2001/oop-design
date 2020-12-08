from person import Person
import random

class Member(Person):
    def __init__(self, name, age, favorite_color, member_id, reward_points):
        # called the __init__ method of the Person class to handle name, age, favorite color
        super().__init__(name, age, favorite_color)
        self.member_id = member_id
        self.reward_points = reward_points
    
    def get_member_id(self):
        print(f'Member id: {self.member_id}')

    def get_points(self):
        print(f'You have {self.reward_points} reward points.')

# omar = Member('Omar', 19, 'red', random.randint(100000,999999), 0)
# omar.introduce()
# omar.fav_color()
# omar.get_member_id()
# omar.get_points()