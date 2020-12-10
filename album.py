from artist import Artist

# class Album inherits from class Artist
class Album(Artist):
    def __init__(self, name, age, artist_name):
        # called the __init__ method of class User to handle name, age, and artist name.
        super().__init__(name, age, artist_name)
        # list is empty so that user can add a new album. 
        self.new_album = []

    # Lil Baby albums + songs.
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
                song = open('albums/lilbaby_3.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/lilbaby_4.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
        
    # Polo G albums + songs.
    def choose_album_2(self):
        choice = input(""" Polo G albums:
        1. The Goat (2020)
        2. Die a Legend (2019)
        """)
        if choice == '1':
            answer = input(""" Choose from the following songs:
            1. Be Something (feat. Lil Baby)
            2. Flex (feat. Juice WRLD)
            """)
            if answer == '1':
                song = open('albums/polog_1.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/polog_2.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
        elif choice == '2':
            answer = input(""" Choose from the following songs:
            1. Pop Out (feat. Lil Tjay)
            2. Effortless
            """)
            if answer == '1':
                song = open('albums/polog_3.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/polog_4.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())

    # Jack Harlow albums + songs.
    def choose_album_3(self):
        choice = input(""" Jack Harlow albums:
        1. Sweet Action (2020)
        2. Thats What They All Say (2020)
        """)
        if choice == '1':
            answer = input(""" Choose from the following songs:
            1. WHATS POPPIN
            2. 2STYLISH
            """)
            if answer == '1':
                song = open('albums/harlow_1.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/harlow_2.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
        elif choice == '2':
            answer = input(""" Choose from the following songs:
            1. Tyler Herro
            2. Way Out (feat. Big Sean)
            """)
            if answer == '1':
                song = open('albums/harlow_3.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/harlow_4.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())

# --------------------------- This represents the end of hip hop/rap artists and start of pop artists ---------------------------------------------------------------------
    
    # Billie Eilish albums + songs.
    def choose_album_4(self):
        choice = input(""" Billie Eilish albums:
        1. When We All Fall Asleep, Where Do We Go? (2019)
        2. dont smile at me (2017)
        """)
        if choice == '1':
            answer = input(""" Choose from the following songs:
            1. bad guy
            2. when the party's over
            """)
            if answer == '1':
                song = open('albums/billie_1.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/billie_2.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
        elif choice == '2':
            answer = input(""" Choose from the following songs:
            1. idontwannabeyouanymore
            2. ocean eyes
            """)
            if answer == '1':
                song = open('albums/billie_3.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/billie_4.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
    
    # The Weeknd albums + songs.
    def choose_album_5(self):
        choice = input(""" The Weeknd albums:
        1. After Hours (2020)
        2. Starboy (2016)
        """)
        if choice == '1':
            answer = input(""" Choose from the following songs:
            1. Heartless
            2. Blinding Lights
            """)
            if answer == '1':
                song = open('albums/weeknd_1.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/weeknd_2.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
        elif choice == '2':
            answer = input(""" Choose from the following songs:
            1. Starboy
            2. I Feel It Coming (feat. Daft Punk)
            """)
            if answer == '1':
                song = open('albums/weeknd_3.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/weeknd_4.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
    
    # Bruno Mars albums + songs.
    def choose_album_6(self):
        choice = input(""" Bruno Mars albums:
        1. 24K Magic (2016)
        2. Unorthodox Jukebox (2012)
        """)
        if choice == '1':
            answer = input(""" Choose from the following songs:
            1. 24K Magic
            2. That's What I Like
            """)
            if answer == '1':
                song = open('albums/bruno_1.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/bruno_2.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
        elif choice == '2':
            answer = input(""" Choose from the following songs:
            1. When I Was Your Man
            2. Locked Out of Heaven
            """)
            if answer == '1':
                song = open('albums/bruno_3.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())
            elif answer == '2':
                song = open('albums/bruno_4.txt', 'r').readlines()
                for line in song:
                    print(line.rstrip())

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

# omar = Album('Omar', 19, 'lil baby')
# omar.choose_album_1()
# omar.choose_album_2()
# omar.choose_album_3()
# omar.choose_album_4()
# omar.choose_album_5()
# omar.choose_album_6()
# omar.add_album('new album')
# omar.show_new_album()