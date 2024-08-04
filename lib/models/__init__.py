import sqlite3

CONN = sqlite3.connect('rigz_finance_tracker')
CURSOR = CONN.cursor()

# Create the transactions table if it doesn't exist
CURSOR.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    date TEXT,
    category TEXT,
    description TEXT,
    trans_type TEXT,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')

# Create the users table if it doesn't exist
CURSOR.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT NOT NULL,
    email TEXT UNIQUE,
    password_hash TEXT
)
''')

CONN.commit()
CONN.close()
