import requests
from bs4 import BeautifulSoup
import time
import sys

# Web sitesinden veri çekmek için bir fonksiyon tanımlama
def veri_cek(url, css_selector):
    # 5 saniye bekleme süresi ekleme
    for i in range(5, 0, -1):
        print(f"{i} ", end="")
        sys.stdout.flush()  # Geri sayımın aynı satırda görünmesi için flush işlemi
        time.sleep(1)  # 1 saniye bekle

    print("\nBekleme süresi bitti. Veri çekiliyor...")

    # HTTP GET isteği gönderme
    response = requests.get(url)

    # İstek başarılıysa devam edelim
    if response.status_code == 200:
        # BeautifulSoup ile HTML içeriğini analiz edelim
        soup = BeautifulSoup(response.content, 'html.parser')

        # Belirtilen CSS seçicisi ile veriyi bulma
        veri = soup.select_one(css_selector)

        if veri:
            return veri.text.strip()  # Veriyi temizleyip döndürelim

    # Hata durumunda veya veri bulunamazsa None döndürme
    return None


# Kullanıcıdan web sitesi adresini ve CSS seçicisini alma
url = input("Web sitesi adresini girin: ")
css_selector = input("CSS selector girin: ")

# Veriyi çekelim
alınan_veri = veri_cek(url, css_selector)

if alınan_veri:
    print("\nAlınan Veri:")
    print(alınan_veri)
else:
    print("\nVeri bulunamadı veya istek yapılamadı.")
