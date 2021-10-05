import requests
from random import randrange
from models.databaseLite import databaseLite
import json


class shopeeDetail:
    image = {}
    catid = 0
    deskripsi = ''
    name = ''
    video = None
    itemid = 0
    shopid = 0
    version = randrange(7, 999999999)
    str_liks = ""
    berat = 500
    mins = 1
    etalase = 0
    kondisi = "Baru"
    sku = "SKID-"+str(randrange(1111111111, 9999999999))
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

    def getData(self, ids):
        link = self.url.replace('?position=', '.')

        links = link.split('-i.')
        linkss = links[1]
        linksss = linkss.split('.')
        self.shopid = linksss[0]
        self.itemid = linksss[1]

        hostlink = "https://shopee.co.id/api/v4/item/get"
        datas = {'itemid': self.itemid,
                 'shopid': self.shopid, 'version': self.version}

        try:

            resp = requests.get(hostlink, params=datas, timeout=30)
            jsons = resp.json()
            i = 0
            for ans in jsons['data']['images']:
                self.image['img'+str(i)] = ans
                i += 1

            self.gambar1 = json.dumps(self.image)

            self.deskripsi = jsons['data']['description'].replace("'", " ")
            self.catid = jsons['data']['catid']

            if jsons['data']['video_info_list'] != '':
                self.video = jsons['data']['video_info_list']
            else:
                self.video = None

            self.video1 = json.dumps(self.video)

            for ansi in jsons['data']['models']:
                prices = str(ansi['price'])
                self.harga = int(prices[0:-5])
                self.stok = ansi['stock']
                if ansi['name'] == '':
                    self.name = jsons['data']['name'].replace("'", "")
                else:
                    self.name = ('['+str(ansi['name'])+"]" +
                                 str(jsons['data']['name'])).replace("'", "")

                self.str_liks = "https://shopee.co.id/" + \
                    str(self.name.replace(" ", "-"))+"-i." + \
                    str(self.shopid)+"."+self.itemid

                dblite = databaseLite()

                dblite.insert_database("tb_detail", "(NULL,'"+str(ids)+"','"+str(self.url)+"','"+str(self.name)+"','"+str(self.deskripsi)+"','"+str(self.catid)+"','"+str(self.berat)+"','"+str(self.mins)+"','"+str(
                    self.etalase)+"','"+str(self.preorder)+"','"+str(self.kondisi)+"','"+str(self.gambar1)+"',NULL,'"+str(self.sku)+"','"+str(self.status)+"','"+str(self.stok)+"','"+str(self.harga)+"','"+str(self.asuransi)+"')")
            return None

        except requests.ConnectionError as error:
            return error
