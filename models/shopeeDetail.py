import requests
from random import randrange


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
    berat = 0
    mins = 1
    etalase = None
    kondisi = "Baru"
    sku = "SKID-"+str(randrange(1111111111, 9999999999))
    stok = 12
    harga = 12000
    url = ""

    def __init__(self, url):
        self.url = url

    def getData(self):
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

            self.deskripsi = jsons['data']['description'].replace("'", " ")
            self.catid = jsons['data']['catid']

            if jsons['data']['video_info_list'] != '':
                self.video = jsons['data']['video_info_list']
            else:
                self.video = None

            for ansi in jsons['data']['models']:
                # self.harga
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

            return None

        except requests.ConnectionError as error:
            return error