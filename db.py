import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, product text, customer text, shop text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM products")
        rows = self.cur.fetchall()
        return rows

    def insert(self, product, customer, shop, price):
        self.cur.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?)",
                         (product, customer, shop, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, product, customer, shop, price):
        self.cur.execute("UPDATE parts SET product = ?, customer = ?, shop = ?, price = ? WHERE id = ?",
                         (product, customer, shop, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

