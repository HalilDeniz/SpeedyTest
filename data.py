import sqlite3

class VeriTabani:
    def __init__(self, veritabani_adi):
        self.veritabani_adi = veritabani_adi
        self.baglanti = None
        self.cursor = None

    def baglan(self):
        self.baglanti = sqlite3.connect(self.veritabani_adi)
        self.cursor = self.baglanti.cursor()

    def tablo_olustur(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS hiz_testi (
                sunucu TEXT,
                ip_adresi TEXT,
                ulke TEXT,
                sehir TEXT,
                ping REAL,
                indirme_hizi REAL,
                yukleme_hizi REAL
            )
        ''')
        self.baglanti.commit()

    def veri_ekle(self, sunucu, ip_adresi, ulke, sehir, ping, indirme_hizi, yukleme_hizi):
        self.cursor.execute('''
            INSERT INTO hiz_testi (sunucu, ip_adresi, ulke, sehir, ping, indirme_hizi, yukleme_hizi)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (sunucu, ip_adresi, ulke, sehir, ping, indirme_hizi, yukleme_hizi))
        self.baglanti.commit()

    def baglantiyi_kapat(self):
        if self.baglanti:
            self.baglanti.close()
