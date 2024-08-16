# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

class SQLitePipeline(object):
    def open_spider(self, spider):
        self.connection = sqlite3.connect('proxies.db')
        self.cursor = self.connection.cursor()
        # Criar a tabela
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS proxies(
                ip_address TEXT NOT NULL PRIMARY KEY,
                port NUMBER,
                code TEXT,
                country TEXT,
                anonimity TEXT,
                google TEXT,
                https TEXT,
                last_checked TEXT
            )
        ''')

        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('''
            INSERT OR IGNORE INTO proxies(ip_address, port, code, country, anonimity, google, https, last_checked) VALUES(?,?,?,?,?,?,?,?)
        ''', (
            item.get('ip_address'),
            item.get('port'),
            item.get('code'),
            item.get('country'),
            item.get('anonimity'),
            item.get('google'),
            item.get('https'),
            item.get('last_checked')
        ))
        self.connection.commit()
        return item 