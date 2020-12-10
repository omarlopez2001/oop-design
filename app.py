from album import Album
from artist import Artist
from genre import Genre
from user import User

# Test code to make sure everything works.

omar = User('Omar Lopez', 19)
omar.greet_user()
omar.user_age()

omar = Genre('omar', 19, 'hiphop/rap')
omar.choose_genre()
omar.add_genre('new genre')
omar.show_new_genre()

omar = Artist('Omar', 19, 'lil baby')
omar.choose_artist_1()
omar.choose_artist_2()
omar.add_artist('new artist')
omar. show_new_artist()

omar = Album('Omar', 19, 'lil baby')
omar.choose_album_1()
omar.choose_album_2()
omar.choose_album_3()
omar.choose_album_4()
omar.choose_album_5()
omar.choose_album_6()
omar.add_album('new album')
omar.show_new_album()
