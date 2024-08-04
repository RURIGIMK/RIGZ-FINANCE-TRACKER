import sqlite3
import hashlib

class User:
    def __init__(self, name, phone, email, password=None, password_hash=None, id=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.id = id
        if password:
            self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        else:
            self.password_hash = password_hash

    def check_password(self, password):
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    def save(self):
        with sqlite3.connect('company.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (name, phone, email, password_hash)
                VALUES (?, ?, ?, ?)
            ''', (self.name, self.phone, self.email, self.password_hash))
            self.id = cursor.lastrowid
            conn.commit()

    @staticmethod
    def find_by_email(email):
        with sqlite3.connect('company.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, name, phone, email, password_hash
                FROM users
                WHERE email = ?
            ''', (email,))
            row = cursor.fetchone()
            if row:
                return User(name=row[1], phone=row[2], email=row[3], password_hash=row[4], id=row[0])
            return None
