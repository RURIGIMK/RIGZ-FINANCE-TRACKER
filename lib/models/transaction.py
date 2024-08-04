import sqlite3

class Transaction:
    def __init__(self, amount, date, category, description, trans_type, user_id=None):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
        self.trans_type = trans_type
        self.user_id = user_id

    def save(self):
        with sqlite3.connect('company.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO transactions (amount, date, category, description, trans_type, user_id)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (self.amount, self.date, self.category, self.description, self.trans_type, self.user_id))
            conn.commit()

    @staticmethod
    def _query(query, params=()):
        with sqlite3.connect('company.db') as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            return [Transaction(amount=row[1], date=row[2], category=row[3], description=row[4], trans_type=row[5], user_id=row[6]) for row in rows]

    @staticmethod
    def all(user_id):
        return Transaction._query('''
            SELECT id, amount, date, category, description, trans_type, user_id
            FROM transactions
            WHERE user_id = ?
        ''', (user_id,))

    @staticmethod
    def filter_by_date(start_date, end_date, user_id):
        return Transaction._query('''
            SELECT id, amount, date, category, description, trans_type, user_id
            FROM transactions
            WHERE date BETWEEN ? AND ? AND user_id = ?
        ''', (start_date, end_date, user_id))

    @staticmethod
    def filter_by_category(category, user_id):
        return Transaction._query('''
            SELECT id, amount, date, category, description, trans_type, user_id
            FROM transactions
            WHERE category = ? AND user_id = ?
        ''', (category, user_id))

    @staticmethod
    def filter_by_type(trans_type, user_id):
        return Transaction._query('''
            SELECT id, amount, date, category, description, trans_type, user_id
            FROM transactions
            WHERE trans_type = ? AND user_id = ?
        ''', (trans_type, user_id))

    @staticmethod
    def filter_by_type_and_category(trans_type, category, user_id):
        return Transaction._query('''
            SELECT id, amount, date, category, description, trans_type, user_id
            FROM transactions
            WHERE trans_type = ? AND category = ? AND user_id = ?
        ''', (trans_type, category, user_id))
