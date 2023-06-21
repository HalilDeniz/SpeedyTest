import speedtest
import sys
import time
from colorama import Fore, Style
import matplotlib.pyplot as plt
from data import VeriTabani

class SpeedTestTool:
    def __init__(self):
        self.st = speedtest.Speedtest()
        self.sunucu = None
        self.indirme_hizi = None
        self.yukleme_hizi = None
        self.ping = None
        self.test_suresi = None

    def get_server_info(self):
        self.sunucu = self.st.get_best_server()

    def download_speed_test_et(self):
        self.indirme_hizi = self.st.download() / 10**6

    def upload_speed_test_et(self):
        self.yukleme_hizi = self.st.upload() / 10**6

    def ping_value_test_et(self):
        self.ping = self.st.results.ping

    def show_results_with_graphs(self):
        etiketler = ['Download', 'Upload', 'Ping']
        hizlar = [self.indirme_hizi, self.yukleme_hizi, self.ping]

        plt.bar(etiketler, hizlar)
        plt.xlabel('Speed Test')
        plt.ylabel('Speed (Mbps)')
        plt.title('Speed Test Results')

        plt.show()

    def loading_animation(self):
        try:
            animasyon = "|/-\\"
            for i in range(20):
                time.sleep(0.1)
                sys.stdout.write(Fore.YELLOW + "\rReceiving data " + animasyon[i % len(animasyon)])
                sys.stdout.flush()
        except KeyboardInterrupt:
            print(".............")
    def start_speed_test(self):
        self.loading_animation()
        print("\n" + Fore.GREEN + "Speed test completed!" + Style.RESET_ALL)
        self.test_suresi = time.time()

    def time_test_time(self):
        if self.test_suresi:
            sure = time.time() - self.test_suresi
            print(f"Speed test time: {sure:.2f} second")
        else:
            print("Speed test not started yet.")

    def show_results(self):
        print(Fore.CYAN + f"Server    : {self.sunucu['sponsor']} - {self.sunucu['name']}")
        print(f"IP Address: {self.sunucu['host']}")
        print(f"Country   : {self.sunucu['country']}")
        print(f"City      : {self.sunucu['name']}")
        print(f"Ping      : {self.ping:.2f} ms")
        print(f"Download  : {self.indirme_hizi:.2f} Mbps")
        print(f"Loading   : {self.yukleme_hizi:.2f} Mbps" + Style.RESET_ALL)

    def save_results(self, dosya_adi):
        with open(dosya_adi, "w") as dosya:
            dosya.write(f"Server    : {self.sunucu['sponsor']} - {self.sunucu['name']}\n")
            dosya.write(f"IP Address: {self.sunucu['host']}\n")
            dosya.write(f"Country   : {self.sunucu['country']}\n")
            dosya.write(f"City      : {self.sunucu['name']}\n")
            dosya.write(f"Ping      : {self.ping:.2f} ms\n")
            dosya.write(f"Download  : {self.indirme_hizi:.2f} Mbps\n")
            dosya.write(f"Loading   : {self.yukleme_hizi:.2f} Mbps\n")
        veritabani = VeriTabani("speed_test.db")
        veritabani.baglan()
        veritabani.tablo_olustur()

        veritabani.veri_ekle(self.sunucu['sponsor'], self.sunucu['host'], self.sunucu['country'],
                             self.sunucu['name'], self.ping, self.indirme_hizi, self.yukleme_hizi)

        veritabani.baglantiyi_kapat()


arac = SpeedTestTool()
arac.get_server_info()
arac.start_speed_test()
arac.download_speed_test_et()
arac.upload_speed_test_et()
arac.ping_value_test_et()
arac.time_test_time()
arac.show_results()
arac.save_results("speed_test_results.txt")
arac.show_results_with_graphs()
