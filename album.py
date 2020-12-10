from artist import Artist
 
class Album(Artist):
    def __init__(self, name, age, artist_name):
        super().__init__(name, age, artist_name)
        self.new_album = []

    def choose_album_1(self):
        choice = input(""" Lil Baby albums:
        1. My turn (2020)
        2. Street Gossip (2018)
        """)
        if choice == '1':
            answer = input(""" Choose from the following songs:
            1. Woah
            2. Emotionally Scarred
            """)
            if answer == '1':
                song = open('albums/lilbaby_1.txt', 'r').readlines()
                # rstrip strips white space characters from only the right end of a string. 
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/lilbaby_2.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
                    
        elif choice == '2':
            answer = input(""" Choose from the following songs:
            1. Global
            2. Time (feat. Meek Mill)
            """)
            if answer == '1':
                print()
            elif answer == '2':
                print()
        
    def choose_album_2(self):
        choice = input(""" Polo G albums:
        1. The Goat (2020)
        2. Die a Legend (2019)
        """)
        if choice == '1':
            print()
        elif choice == '2':
            print()

    def choose_album_3(self):
        choice = input(""" Jack Harlow albums:
        1. Sweet Action (2020)
        2. Thats What They All (2020)
        """)
        if choice == '1':
            print()
        elif choice == '2':
            print()
        
    def choose_album_4(self):
        choice = input(""" Billie Eilish albums:
        1. When We All Fall Asleep, Where Do We Go? (2019)
        2. Live at Third Man Records (2019)
        """)
        if choice == '1':
            print()
        elif choice == '2':
            print()
    
    def choose_album_5(self):
        choice = input(""" The Weeknd albums:
        1. After Hours (2020)
        2. Starboy (2016)
        """)
        if choice == '1':
            print()
        elif choice == '2':
            print()
    
    def choose_album_6(self):
        choice = input(""" Bruno Mars albums:
        1. 24K Magic (2016)
        2. Unorthodox Jukebox (2012)
        """)
        if choice == '1':
            print()
        elif choice == '2':
            print()

    def add_album(self, album):
        choice = input(""" Would you like to add a new album?
        1. yes
        2. no        
        """)
        if choice == '1':
            answer = input('Great, please insert the name of the album you would like to add.')
            album = answer
            self.new_album.append(album)
        else:
            print(f'Have a great day!')
        
    def show_new_album(self):
        for album in self.new_album:
            print(f'The following album has been added: {album}')

omar = Album('Omar', 19, 'lil baby')
omar.choose_album_1()
omar.choose_album_2()
omar.choose_album_3()
omar.choose_album_4()
omar.choose_album_5()
omar.choose_album_6()
omar.add_album('new album')
omar.show_new_album()
