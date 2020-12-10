from user import User

# class Genre inherits from class User.
class Genre(User):
    def __init__(self, name, age, genre):
        # called the __init__ method of class User to handle name and age.
        super().__init__(name, age)
        self.genre = genre
        # list is empty so that user can add a new genre. 
        self.new_genre = []

    def choose_genre(self):
        choice = input(""" Please choose a genre: 
        1. hiphop/rap
        2. pop
        3. Other
        """)
        if choice == '1':
            print(f'You have chosen hiphop/rap.')
        elif choice == '2':
            print(f'You have chosen pop.')
        elif choice == '3':
            print(f'Sorry, these are all the genres we currently have.')
        
    def add_genre(self, genres):
        choice = input(""" Would you like to add a genre?
        1. yes
        2. no        
        """)
        if choice == '1':
            answer = input('Great, what genre would you like to add?')
            genres = answer
            self.new_genre.append(genres)
        else:
            print(f'Have a great day!')
        
    def show_new_genre(self):
        for genres in self.new_genre:
            print(f'The following genre has been added: {genres}')
            

# omar = Genre('omar', 19, 'hiphop/rap')
# omar.choose_genre()
# omar.add_genre('new genre')
# omar.show_new_genre()