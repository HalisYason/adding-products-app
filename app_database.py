

import sqlite3 as sql
import os

# db_file = os.path.join(os.getcwd(), "database", "urunler.db")

# vt = sql.connect(db_file)

vt = sql.connect("urunler.db")    # exe alırken database klasöründen çıkarmak gerekir çünkü exe bu yolu bulamaz.

cursor = vt.cursor()

cursor.execute("""create table if not exists urun(

    urun_kod text,
    urun_ad text,
    urun_fiyat integer,
    urun_stok integer,
    urun_kategori text

)""")

vt.commit()
vt.close()


# veritabanına ürün ekleme
def vt_urun_ekle(kod=None,ad=None,fiyat=None,stok=None,kategori=None):  
    vt = sql.connect("urunler.db")
    cursor = vt.cursor()



    if kod != None and ad != None and fiyat != None and stok != None and kategori != None:
        fiyat = int(fiyat)
        stok = int(stok)
        data = (kod,ad,fiyat,stok,kategori)
        cursor.execute("insert into urun values(?,?,?,?,?)",data)


    vt.commit()
    vt.close()




# veritabanındaki ürünü koduna bakarak siler
def vt_urun_sil(kod):
    vt = sql.connect("urunler.db")
    cursor = vt.cursor()  

    try:
        cursor.execute(f"delete from urun where urun_kod={kod}")
    except sql.OperationalError:
        pass


    vt.commit()
    vt.close()



# bütün ürünleri getirir
def vt_butun_urun_listele():

    with sql.connect("urunler.db") as vt:

        cursor = vt.cursor()  

        data = cursor.execute("select * from urun")

        return data
    

    
# istenilen kategorideki ürünleri getirir
def vt_ozel_urun_listele(kategori):
    with sql.connect("urunler.db") as vt:
        cursor = vt.cursor()  

        data = cursor.execute(f"select * from urun where urun_kategori='{kategori}'")

        return data
    


 
