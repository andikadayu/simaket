import sqlite3
from pathlib import Path


class databaseLite:

    pathdb = str(Path().absolute())+'/tools/scrapping.db'

    def __init__(self) -> None:
        pass

    def read_dateabase(self, table, select, join, where, limit):
        try:
            con = sqlite3.connect(self.pathdb)

            sql = "SELECT "+select+" FROM "+table+" "

            if join != '':
                sql += ''+join+" "

            if where != '':
                sql += ''+where+" "

            if limit != '':
                sql += ''+limit+" "

            cur = con.cursor()
            cur.execute(sql)
            row = cur.fetchall()

            return row

        except sqlite3.Error as e:
            return e

    def insert_database(self, table, values):
        try:
            con = sqlite3.connect(self.pathdb)

            sql = "INSERT INTO "+table+" VALUES"+values

            con.execute(sql)

            con.commit()

            con.close()

        except sqlite3.Error as e:
            return e

    def insert_getId(self, table, values):
        try:
            con = sqlite3.connect(self.pathdb)

            ids = 0
            sql = "INSERT INTO "+table+" VALUES"+values

            cur = con.cursor()

            cur.execute(sql)

            con.commit()
            ids = cur.lastrowid
            con.close()

            return ids

        except sqlite3.Error as e:
            return e

    def truncate_database(self):
        try:
            con = sqlite3.connect(self.pathdb)

            sql = "DELETE FROM tb_lazada;DELETE FROM tb_shopee;DELETE FROM tb_scrap;DELETE FROM sqlite_sequence WHERE name = 'tb_scrap';DELETE FROM sqlite_sequence WHERE name = 'tb_lazada';DELETE FROM sqlite_sequence WHERE name = 'tb_shopee'; "

            con.executescript(sql)

            con.commit()

            con.close()

        except sqlite3.Error as e:
            return e
