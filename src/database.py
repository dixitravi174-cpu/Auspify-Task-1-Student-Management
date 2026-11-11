import sqlite3

DATABASE_NAME = "students.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # Dict format me rows access karne ke liye
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Students table create karna
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            course TEXT NOT NULL,
            phone TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database aur 'students' table successfully initialize ho gaye!")

if __name__ == "__main__":
    init_db()