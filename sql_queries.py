
# DROP TABLES
drop_table_queries = [
    "DROP TABLE IF EXISTS songplays",
    "DROP TABLE IF EXISTS users",
    "DROP TABLE IF EXISTS songs",
    "DROP TABLE IF EXISTS artists",
    "DROP TABLE IF EXISTS time",
    "DROP TABLE IF EXISTS staging_events",
    "DROP TABLE IF EXISTS staging_songs"
]

# CREATE TABLES
create_table_queries = [

"""CREATE TABLE IF NOT EXISTS staging_events (
artist VARCHAR, auth VARCHAR, firstName VARCHAR, gender VARCHAR,
itemInSession INT, lastName VARCHAR, length FLOAT, level VARCHAR,
location VARCHAR, method VARCHAR, page VARCHAR, registration BIGINT,
sessionId INT, song VARCHAR, status INT, ts BIGINT,
userAgent VARCHAR, userId INT);""",

"""CREATE TABLE IF NOT EXISTS staging_songs (
num_songs INT, artist_id VARCHAR, artist_latitude FLOAT,
artist_longitude FLOAT, artist_location VARCHAR, artist_name VARCHAR,
song_id VARCHAR, title VARCHAR, duration FLOAT, year INT);""",

"""CREATE TABLE IF NOT EXISTS songplays (
songplay_id INT IDENTITY(0,1),
start_time TIMESTAMP, user_id INT, level VARCHAR,
song_id VARCHAR, artist_id VARCHAR, session_id INT,
location VARCHAR, user_agent VARCHAR);""",

"""CREATE TABLE IF NOT EXISTS users (
user_id INT PRIMARY KEY, first_name VARCHAR,
last_name VARCHAR, gender VARCHAR, level VARCHAR);""",

"""CREATE TABLE IF NOT EXISTS songs (
song_id VARCHAR PRIMARY KEY, title VARCHAR,
artist_id VARCHAR, year INT, duration FLOAT);""",

"""CREATE TABLE IF NOT EXISTS artists (
artist_id VARCHAR PRIMARY KEY, name VARCHAR,
location VARCHAR, latitude FLOAT, longitude FLOAT);""",

"""CREATE TABLE IF NOT EXISTS time (
start_time TIMESTAMP PRIMARY KEY,
hour INT, day INT, week INT, month INT, year INT, weekday INT);"""
]

# COPY + INSERT
copy_table_queries = []

insert_table_queries = [

"""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
SELECT TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second',
userId, level, song_id, artist_id, sessionId, location, userAgent
FROM staging_events;""",

"""INSERT INTO users
SELECT DISTINCT userId, firstName, lastName, gender, level
FROM staging_events;""",

"""INSERT INTO songs
SELECT song_id, title, artist_id, year, duration
FROM staging_songs;""",

"""INSERT INTO artists
SELECT artist_id, artist_name, artist_location, artist_latitude, artist_longitude
FROM staging_songs;""",

"""INSERT INTO time
SELECT DISTINCT TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second',
EXTRACT(hour FROM TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second'),
EXTRACT(day FROM TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second'),
EXTRACT(week FROM TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second'),
EXTRACT(month FROM TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second'),
EXTRACT(year FROM TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second'),
EXTRACT(dow FROM TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second')
FROM staging_events;"""
]
