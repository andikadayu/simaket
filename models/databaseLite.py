import sqlite3
from pathlib import Path


class databaseLite:

    pathdb = str(Path().absolute())+'/tools/scrapping.db'

    def __init__(self) -> None:
        pass

    def read_dateabase(self):
        try:
            con = sqlite3.connect(self.pathdb)
        except sqlite3.Error as e:
            print(e)
