
from PyQt5.QtWidgets import *
from ui.main_python import *

from PyQt5.QtWidgets import QTableWidgetItem

from dark_mode import set_dark_mode_stylesheet

from database.app_database import *


class mainPage( QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = Ui_MainWindow()
        self.main.setupUi(self)

        # butonlar
        self.main.pushButton_ekle.clicked.connect(self.urun_ekle)
        self.main.pushButton_sil.clicked.connect(self.urun_silme)
        self.main.pushButton_urun_listele.clicked.connect(self.urun_listele)

        # dark mod checkbox
        self.main.checkBox_darkmode.stateChanged.connect(self.toggle_dark_mode)


    # urun ekle
    def urun_ekle(self):
        kod = self.main.lineEdit_urun_kod.text()
        ad = self.main.lineEdit_urun_ad.text()
        fiyat = self.main.lineEdit_urun_fiyat.text()
        stok = self.main.lineEdit_urun_stok.text()
        kategori = self.main.comboBox_kategori_ekle.currentText()

        try:
            vt_urun_ekle(kod,ad,fiyat,stok,kategori)
            if kod !="" and ad !="" and fiyat !="" and stok !="" and kategori != "":
                # ekranda mesaj gösterir
                self.main.statusbar.showMessage("ürün eklendi",2000)
                self.urun_listele()
        except Exception as error:
            if kod =="" and ad =="" and fiyat =="" and stok =="" and kategori == "":
                self.main.statusbar.showMessage("ürün eklenemedi ===" + str(error),2000)

        

        self.main.lineEdit_urun_kod.clear()
        self.main.lineEdit_urun_ad.clear()
        self.main.lineEdit_urun_fiyat.clear()
        self.main.lineEdit_urun_stok.clear()


    # tabloda ürünleri listeleme
    def urun_listele(self):
        self.main.tableWidget_urun_tablo.clear()
        self.main.tableWidget_urun_tablo.setHorizontalHeaderLabels(("urun kod","urun ad","fiyat","stok","kategori"))


        # burada eğer listelenecek ürünler fazlaysa onları sıkıştırıp ekrana sığmasını sağlar.
        self.main.tableWidget_urun_tablo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # veritabanından gelen verileri açıp tabloya uydurma işlemi
        if self.main.comboBox_katogori_listele.currentText() == "hepsi":
            data = vt_butun_urun_listele()
            for indexSatir, kayitNumarasi in enumerate(data):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    self.main.tableWidget_urun_tablo.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))
        else:
            listele_kategori_adi = self.main.comboBox_katogori_listele.currentText()
            data = vt_ozel_urun_listele(listele_kategori_adi)
            for indexSatir, kayitNumarasi in enumerate(data):
                for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                    self.main.tableWidget_urun_tablo.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))


    # urun silme
    def urun_silme(self):
        kod = self.main.lineEdit_sil_urun_kod.text()

        if kod !="":
            vt_urun_sil(kod)
            self.main.statusbar.showMessage("ürün silindi",2000)
            self.urun_listele()
        if kod == "":
            self.main.statusbar.showMessage("ürün silinemedi",2000)
        

        self.main.lineEdit_sil_urun_kod.clear()

    
    # dark mod aktif olunca
    def toggle_dark_mode(self, state):
        if state:
            dark_stylesheet = set_dark_mode_stylesheet()
            self.setStyleSheet(dark_stylesheet)
        else:
            self.setStyleSheet('')












