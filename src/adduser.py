import sqlite3
import hashlib
import os

# Get curr path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = BASE_DIR + "/quiz.db"


def addUser(user, pwd, type):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        'Insert into USER(user,pass,type) values("{0}","{1}","{2}");'.format(
            user, pwd, type
        )
    )
    conn.commit()
    conn.close()


with open(BASE_DIR + "/users.csv", "r") as file:
    lines = file.read().splitlines()

for users in lines:
    (user, type) = users.split(",")
    print(user)
    print(type)
    addUser(user, hashlib.md5(user.encode()).hexdigest(), type)
