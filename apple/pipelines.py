import sqlite3

class ApplePipeline(object):
    def __init__(self):
        self.create_database()
        self.create_table()

    def create_database(self):
        self.conn = sqlite3.connect('macbook_price.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute('''DROP TABLE IF EXISTS base_model_price''')
        self.curr.execute('''CREATE TABLE base_model_price (list INTEGER PRIMARY KEY AUTOINCREMENT, 
        location TEXT, price TEXT)''')

    def process_item(self, item, spider):
        self.store_item(item)
        return item

    def store_item(self, item):
        self.curr.execute('''INSERT INTO base_model_price (location, price) VALUES (?,?)''',
                          (item['location'][0], item['price'][0]))

        self.conn.commit()