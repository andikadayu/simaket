from random import randrange
import json

from models.databaseLite import databaseLite


class lazadaDetail:
    image = {}
    catid = 0
    deskripsi = ''
    name = ''
    video = None
    itemid = 0
    shopid = 0
    version = randrange(7, 999999999)
    str_liks = ""
    berat = 0
    mins = 1
    etalase = None
    kondisi = "Baru"
    sku = ""
    stok = 12
    harga = 12000
    url = ""
    gambar1 = ""
    video1 = ""
    preorder = 0
    status = "Aktif"
    asuransi = "optional"

    def __init__(self, url):
        self.url = url

    def getData(self, data, image, ids):
        self.gambar1 = image.replace("80x80", "1080x720")
        js = json.loads(data)

        self.name = js['name'].replace("'", "")
        self.harga = js['offers']['lowPrice']
        self.deskripsi = js['description'].replace("'", "")
        self.sku = js['sku']

        dblite = databaseLite()

        dblite.insert_database("tb_lazada", "(NULL,'"+str(ids)+"','"+str(self.url)+"','"+str(self.name)+"','"+str(self.deskripsi)+"','"+str(self.catid)+"','"+str(self.berat)+"','"+str(self.mins)+"','"+str(
            self.etalase)+"','"+str(self.preorder)+"','"+str(self.kondisi)+"','"+str(self.gambar1)+"',NULL,'"+str(self.sku)+"','"+str(self.status)+"','"+str(self.stok)+"','"+str(self.harga)+"','"+str(self.asuransi)+"')")

        return None
