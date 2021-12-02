import sqlalchemy

db = 'postgresql://ivoronkov:u123456@localhost:5432/ivoronkov'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


# connection.execute("""INSERT INTO track(id, track_name, album_id)
#     VALUES(91, 'all that she wants', 97);
# """)


# connection.execute("""UPDATE track
#     SET duration = 210
#     WHERE id = 91;
# """)


# connection.execute("""UPDATE track
#     SET album_id = 100
#     WHERE id = 90;
# """)


