import sqlite3

DB_PATH = "quiz.db"

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with open('quiz.sql') as file:
        cursor.executescript(file.read())
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db()