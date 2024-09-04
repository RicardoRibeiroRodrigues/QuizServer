import sqlite3
import os


# Get curr path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = BASE_DIR + '/quiz.db'

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with open(BASE_DIR + "/quiz.sql") as file:
        cursor.executescript(file.read())
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db()