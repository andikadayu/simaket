
# test database

# from models.databaseLite import databaseLite

# dblite = databaseLite()
# rows = dblite.read_dateabase("tb_scrap", "*", "", "", "", "", "")
# for row in rows:
#     print(row)
# print(dblite.insert_getId('tb_scrap', "(NULL,'2021-10-02','1')"))
# dblite.truncate_database()
# print(dblite.get_count("tb_scrap", "id_scrap", ""))

# test shopee detail

# from models.shopeeDetail import shopeeDetail
# from models.databaseLite import databaseLite
# dblite = databaseLite()

# ids = dblite.insert_getId('tb_scrap', "(NULL,'2021-10-02','1')")
# detail = shopeeDetail(
#     "https://shopee.co.id/Osaka-Set-Sprei-dan-Bed-Cover-JTI-157-Jacquard-Tencel-i.8534891.8841313151")
# print(detail.getData(ids))

# Lazada Testing

# from models.databaseLite import databaseLite
# from models.lazadaDetail import lazadaDetail
# from models.lazadaItem import lazadaItem
# import json

# dblite = databaseLite()
# ids = dblite.insert_getId('tb_scrap', "(NULL,'2021-10-02','2')")

# urls = "https://www.lazada.co.id/products/charger-oppo-30-a-pengisian-cepat-kabel-data-casan-oppo-a37-a57-a3s-a5s-f1s-f1plus-f3-f5-cas-oppo-i4818186342-s8837964868.html"
# lazitem = lazadaItem(urls)


# jsdata = lazitem.getData()
# jsimage = json.dumps(lazitem.getImage())

# lazdet = lazadaDetail(urls)
# print(lazdet.getData(jsdata, jsimage, ids))

# lazitem.shutDown()

# test xlsx


# from models.excelCreate import excelcreate

# xlsx = excelcreate()

# xlsx.create_excel(limit=5, offset=0, shop=1)
