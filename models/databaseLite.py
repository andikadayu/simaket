import sqlite3
from pathlib import Path


class databaseLite:

    pathdb = str(Path().absolute())+'/tools/scrapping.db'

    def __init__(self) -> None:
        pass

    def read_dateabase(self, table, select, join, where, groupby, orderby, limit):
        try:
            con = sqlite3.connect(self.pathdb)

            sql = "SELECT "+select+" FROM "+table+" "

            if join != '':
                sql += join+" "

            if where != '':
                sql += "WHERE "+where+" "

            if groupby != '':
                sql += "Group By "+groupby+" "

            if orderby != '':
                sql += "Order By "+orderby+" "

            if limit != '':
                sql += "Limit "+limit+" "

            cur = con.cursor()
            cur.execute(sql)
            row = cur.fetchall()

            return row

        except sqlite3.Error as e:
            return e

    def get_count(self, table, wcount, where):
        try:
            con = sqlite3.connect(self.pathdb)

            sql = "SELECT COUNT("+wcount+") FROM "+table+" "

            if where != '':
                sql += "WHERE "+where+" "

            cur = con.cursor()
            cur.execute(sql)
            row = cur.fetchone()

            return row[0]

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

            sql = "DELETE FROM tb_lazada;DELETE FROM tb_shopee;DELETE FROM tb_scrap;DELETE FROM tb_detail;DELETE FROM sqlite_sequence WHERE name = 'tb_scrap';DELETE FROM sqlite_sequence WHERE name = 'tb_lazada';DELETE FROM sqlite_sequence WHERE name = 'tb_shopee';DELETE FROM sqlite_sequence WHERE name = 'tb_detail'; "

            con.executescript(sql)

            con.commit()

            con.close()

        except sqlite3.Error as e:
            return e
