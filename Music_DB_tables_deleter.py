import sqlalchemy

db = 'postgresql://ivoronkov:u123456@localhost:5432/ivoronkov'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

connection.execute("""INSERT INTO artist(id, artist_name)
    VALUES(1, 'queen');
""")

connection.execute("""DELETE FROM artist
""")

connection.execute("""DELETE FROM album
""")

connection.execute("""DELETE FROM genre
""")

connection.execute("""DELETE FROM track
""")

connection.execute("""DELETE FROM collection
""")

connection.execute("""DELETE FROM artist_album
""")

connection.execute("""DELETE FROM artist_genre
""")

connection.execute("""DELETE FROM collection_track
""")
