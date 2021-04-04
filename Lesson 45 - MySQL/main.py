import sqlite3, requests

words = []
with requests.get("https://raw.githubusercontent.com/dolph/dictionary/master/popular.txt") as file:
    for line in file.text.split():
        words.append(line)
# print(words)

with sqlite3.connect("database.db") as connection:
    # print("Connected to database")
    # query = "CREATE TABLE IF NOT EXISTS words (word TEXT PRIMARY KEY)"
    # connection.execute(query)

    # for word in words:
    #     query = "INSERT INTO words (word) VALUES ('{}')".format(word)
    #     print(query)
    #     connection.execute(query)

    # query = "SELECT * FROM words WHERE word LIKE 'y%'"
    # result = connection.execute(query)
    # print(result.fetchall())
    # print(result.fetchone())

    query = "SELECT MAX(LENGTH(word)) FROM words"
    result = connection.execute(query)
    length = result.fetchone()[0]

    query = "SELECT word FROM words WHERE LENGTH(word) = {}".format(length)
    result = connection.execute(query)
    print(result.fetchall())

    query = "SELECT word FROM words WHERE LENGTH(word) = (SELECT MAX(LENGTH(word)) FROM words)"
    result = connection.execute(query)
    print(result.fetchall())

    query = "SELECT word FROM words ORDER BY LENGTH(word) DESC"
    result = connection.execute(query)
    length = 0
    while len((word := result.fetchone())[0]) >= length:
        print(word)
        length = len(word[0])