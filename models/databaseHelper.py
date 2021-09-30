import pymysql
import yaml
from pathlib import Path


class databaseHelper:

    conn = pymysql.NULL
    config = yaml.load(open(str(Path().absolute())+'/config/database.yaml', 'r'),
                       Loader=yaml.FullLoader)
    host = config['host']
    user = config['user']
    pasw = config['pass']
    db = config['db']

    def __init__(self):
        pass

    def open_connection(self):
        try:
            self.conn = pymysql.connect(
                host=self.host, user=self.user, passwd=self.pasw, db=self.db, cursorclass=pymysql.cursors.DictCursor)
        except pymysql.Error as e:
            return e

    def close_connection(self):
        self.conn.close()

    def read_database(self, tabel, select, join, where, limit):
        self.open_connection()
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    sql = "Select "+select+" FROM "+tabel+" "

                    if join != '':
                        sql += ''+join+" "

                    if where != '':
                        sql += ''+where+" "

                    if limit != '':
                        sql += ''+limit+" "

                    cursor.execute(sql)
                    result = cursor.fetchall()

                    self.close_connection()
                    return result
        except pymysql.Error as e:
            return e

    def insert_database(self, tabel, value):
        self.open_connection()
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    sql = "INSERT INTO "+tabel+" VALUES"+value

                    cursor.execute(sql)
                self.conn.commit()
                self.close_connection()
        except pymysql.Error as e:
            return e
