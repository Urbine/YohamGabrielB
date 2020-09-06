SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Artist JOIN Album JOIN Genre ON Track.album_id = Album.id AND Track.genre_id = Genre.id AND Album.artist_id = Artist.id