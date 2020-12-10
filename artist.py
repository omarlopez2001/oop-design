from user import User

# class Artist inherits from class User.
class Artist(User):
    def __init__(self, name, age, artist_name):
        # called the __init__ method of class User to handle name and age.
        super().__init__(name, age)
        self.artist_name = artist_name
        # list is empty so that user can add a new artist. 
        self.new_artist = []
    
    # hiphop/rap artists
    def choose_artist_1(self):
        choice = input(""" Please choose from the following artists:
        1. Lil Baby
        2. Polo G
        3. Jack Harlow
        4. Other
        """)
        if choice == '1':
            print(f'Lil Baby is an American rapper, singer, and songwriter from Atlanta, Georgia. ')
        elif choice == '2':
            print(f'Polo G is an American rapper, singer, songwriter, and record executive from Chicago, Illinois. ')
        elif choice == '3':
            print(f'Jack Harlow is an American rapper and songwriter from Shelbyville, Kentucky. ')
        elif choice == '4':
            print(f'Sorry, these are all the artists we currently have. ')
    
    # pop artists
    def choose_artist_2(self):
        choice = input(""" Please choose from the following artists:
        1. Billie Eilish
        2. The Weeknd
        3. Bruno Mars
        4. Other
        """)
        if choice == '1':
            print(f'Billie Eilish is an American singer-songwriter from Los Angeles, California. ')
        elif choice == '2':
            print(f'The Weeknd is a Canadian singer, songwriter, and record producer from Toronto, Canada. ')
        elif choice == '3':
            print(f'Bruno Mars is an American singer, songwriter, record producer, musician, and dancer from Honolulu, Hawaii. ')
        elif choice == '4':
            print(f'Sorry, these are all the artists we currently have. ')
        
    def add_artist(self, artist):
        choice = input(""" Would you like to add a new artist?
        1. yes
        2. no        
        """)
        if choice == '1':
            answer = input('Great, please insert the name of the artist you would like to add.')
            artist = answer
            self.new_artist.append(artist)
        else:
            print(f'Have a great day!')
        
    def show_new_artist(self):
        for artist in self.new_artist:
            print(f'The following artist has been added: {artist}')

omar = Artist('Omar', 19, 'lil baby')
omar.choose_artist_1()
omar.choose_artist_2()
omar.add_artist('new artist')
omar. show_new_artist()