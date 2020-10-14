import datetime

def build_init_test_db_command(app, db, **kwargs):
  @app.cli.command("init_test_db")
  def prepare_db_for_test():
    """Drops and Creates fresh database"""
    db.drop_all()
    db.create_all()

    album_element1 = kwargs["Album"](album_id="1", name="First album test", 
                          album_type="Single", 
                          release_date="Thu, 09 Jan 2020 00:00:00 GMT", 
                          total_tracks="1")
    db.session.add(album_element1)

    album_element2 = kwargs["Album"](album_id="2", name="Second album", 
                          album_type="Single", 
                          release_date="Fri, 09 Oct 2020 00:00:00 GMT", 
                          total_tracks="1")
    db.session.add(album_element2)

    album_element3 = kwargs["Album"](album_id="3", name="Third album", 
                          album_type="Single", 
                          release_date="Fri, 02 Oct 2020 00:00:00 GMT", 
                          total_tracks="1")
    db.session.add(album_element3)

    artist_element1 = kwargs["Artist"](artist_id="1", name="Nabil")
    db.session.add(artist_element1)

    artist_element2 = kwargs["Artist"](artist_id="2", name="ZINE")
    db.session.add(artist_element2)

    artist_element3 = kwargs["Artist"](artist_id="3", name="Feat")
    db.session.add(artist_element3)

    album_element1.artists.append(artist_element1)
    # artist_element1.albums.append(album_element1)

    album_element2.artists.append(artist_element2)
    # artist_element2.albums.append(album_element2)

    album_element3.artists.extend((artist_element2, artist_element3))
    # artist_element2.albums.append(album_element3)
    # artist_element3.albums.append(album_element3)


    db.session.commit()

    print("Initialized default DB")

