from openpyxl import load_workbook
from pathlib import Path

from models.databaseLite import databaseLite


class excelcreate:
    def __init__(self) -> None:
        pass

    def create_excel(self, limit, offset, shop, nama_file, preorder, etalase, kategori, markupv, berat, min_pesan, stok, hapus_kata):
        dblite = databaseLite()
        if shop == 1:
            tball = dblite.read_dateabase(table="tb_detail", select="tb_detail.*", join="INNER JOIN tb_scrap ON tb_scrap.id_scrap = tb_detail.id_scrape",
                                          where="tb_scrap.id_commerce='"+str(shop)+"' AND jumlah_stok >= "+str(stok), groupby="", orderby="", limit=str(limit), offset=str(offset))
        else:
            tball = dblite.read_dateabase(table="tb_detail", select="tb_detail.*", join="INNER JOIN tb_scrap ON tb_scrap.id_scrap = tb_detail.id_scrape",
                                          where="tb_scrap.id_commerce='"+str(shop)+"'", groupby="", orderby="", limit=str(limit), offset=str(offset))

        spreadsheet = load_workbook(
            str(Path().absolute())+"/tools/templetes.xlsx")
        sheet = spreadsheet.active
        sheet.append([""])
        if shop == 1:
            for row in tball:
                # Markup Price
                markup = int(row[16]) * int(markupv) / 100
                price = int(row[16]) + int(markup)

                # remove text
                nama = row[3]
                deskripsi = row[4]

                if hapus_kata != '':
                    rtext = hapus_kata.split(',')
                    for ans in rtext:
                        nama.replace(ans, '')
                        deskripsi.replace(ans, '')

                # image selection
                img = row[11].replace(
                    "[", "").replace("]", "").replace('"', '')
                imgr = img.split(',')
                cimgr = len(imgr)

                sheet.append(["", nama, deskripsi, kategori, berat, min_pesan, etalase, preorder,
                              row[10], "https://f.shopee.co.id/file/"+str(imgr[0]) if cimgr >= 1 else "", "https://f.shopee.co.id/file/"+str(imgr[1]) if cimgr >= 2 else "", "https://f.shopee.co.id/file/"+str(imgr[2]) if cimgr >= 3 else "", "https://f.shopee.co.id/file/"+str(imgr[3]) if cimgr >= 4 else "", "https://f.shopee.co.id/file/"+str(imgr[4]) if cimgr >= 5 else "", "", "", "", row[13], row[14], row[15], round(price), row[17]])
        elif shop == 2:
            for row in tball:
                # Markup Price
                markup = int(row[16]) * int(markupv) / 100
                price = int(row[16]) + int(markup)

                # remove text
                nama = row[3]
                deskripsi = row[4]

                if hapus_kata != '':
                    rtext = hapus_kata.split(',')
                    for ans in rtext:
                        nama.replace(ans, '')
                        deskripsi.replace(ans, '')

                # image selection
                img = row[11].replace(
                    "[", "").replace("]", "").replace('"', '')
                imgr = img.split(',')
                cimgr = len(imgr)
                sheet.append(["", nama, deskripsi, kategori, berat, min_pesan, etalase, preorder,
                              row[10], str(imgr[0]) if cimgr >= 1 else "", str(imgr[1]) if cimgr >= 2 else "", str(imgr[2]) if cimgr >= 3 else "", str(imgr[3]) if cimgr >= 4 else "", str(imgr[4]) if cimgr >= 5 else "", "", "", "", row[13], row[14], stok, round(price), row[17]])

        else:
            return None

        spreadsheet.save(str(Path().absolute()) +
                         "/export/"+str(nama_file)+"-"+str(offset)+".xlsx")
