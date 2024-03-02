from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Kullanıcıdan web sitesi adresini al
url = input("Web sitesi adresini girin: ")

# Tarayıcıyı başlat
driver = webdriver.Firefox()

# Siteye git
driver.get(url)

# Kullanıcıdan "Nereden?" bilgisini al ve lowercase yaparak uygun yere yaz
nereden = input("Nereden? ").lower()
driver.find_element(By.CSS_SELECTOR, '#from_text').send_keys(nereden)

# Kullanıcıdan "Nereye?" bilgisini al ve lowercase yaparak uygun yere yaz
nereye = input("Nereye? ").lower()
driver.find_element(By.CSS_SELECTOR, '#to_text').send_keys(nereye)

# Kullanıcıdan seyahat tipini al
seyahat_tipi = input("Gidis dönüş mü? Tek yon mu? ")

if seyahat_tipi.lower() == "gidis dönüs":
    # Gidiş dönüş seçeneği için checkbox'ı işaretleyin
    driver.find_element(By.CSS_SELECTOR, '#rbRoundtrip').click()
'''
# Kullanıcıdan alınan ay kısaltmalarını ve karşılık gelen İngilizce ay isimlerini içeren bir sözlük
ay_karsiliklari = {
    "ocak": "Oca",
    "şubat": "Şub",
    "mart": "Mar",
    "nisan": "Nis",
    "mayıs": "May",
    "haziran": "Haz",
    "temmuz": "Tem",
    "ağustos": "Ağu",
    "eylül": "Eyl",
    "ekim": "Eki",
    "kasım": "Kas",
    "aralık": "Ara"
}

# Kullanıcıdan alınan tarihi işleyerek uygun formata dönüştürün (örn. 9 aralık 2023)
kullanici_tarihi = input("Tarihi girin (Örn. 9 aralık 2023): ")
parcalanmis_tarih = kullanici_tarihi.lower().split()  # Tüm harfleri küçült ve parçala

# Gün, ay ve yılı parçala
gun = parcalanmis_tarih[0].zfill(2)  # Tek haneli günler için başına 0 ekle
ay = ay_karsiliklari.get(parcalanmis_tarih[1], "")  # Girilen ayı karşılığına dönüştür
yil = parcalanmis_tarih[2]

# Oluşturulan tarih bilgilerini ayrı <td> etiketlerine yerleştirin
gun_td_selector = '#traditionalSearch > div.col-lg-11.col-md-12.pr-1 > div:nth-child(1) > div > div.col-lg-4.col-sm-12.col-12.pl-3.pl-md-0 > div > div.col-md-4.col-6.datepicker-box.where-date-go.search-col > div > div > button > table > tbody > tr > td.tdday'
ay_yil_td_selector = '#traditionalSearch > div.col-lg-11.col-md-12.pr-1 > div:nth-child(1) > div > div.col-lg-4.col-sm-12.col-12.pl-3.pl-md-0 > div > div.col-md-4.col-6.datepicker-box.where-date-go.search-col > div > div > button > table > tbody > tr > td:nth-child(2)'


# Belirli bir düğmeye tıklamadan önce beklemek için düğmenin CSS seçicisini tanımlayın
dugme_selector = '#traditionalSearch > div.col-lg-11.col-md-12.pr-1 > div:nth-child(1) > div > div.col-lg-4.col-sm-12.col-12.pl-3.pl-md-0 > div > div.col-md-4.col-6.datepicker-box.where-date-go.search-col > div > div > button'

# Düğmenin etkileşilebilir olmasını bekleyin
dugme = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, dugme_selector))
)
# Düğmeye tıklayın
dugme.click()

# Bekleme süresi ekleyin (2 saniye gibi)
driver.implicitly_wait(2)

# Gün bilgisini belirtilen <td> etiketine yerleştirin
driver.find_element(By.CSS_SELECTOR, gun_td_selector).send_keys(gun)

# Ay ve yıl bilgilerini uygun formatta birleştirin (Ara 2023)
ay_yil_birlesik = f"{ay} {yil}"

# Ay ve yıl bilgisini belirtilen <td> etiketine yerleştirin
driver.find_element(By.CSS_SELECTOR, ay_yil_td_selector).send_keys(ay_yil_birlesik)

# Eğer gidiş-dönüş seçeneği seçildiyse dönüş tarihini de al
if seyahat_tipi.lower() == "gidis dönüs":
    kullanici_tarihi = input("Donus tarihi girin (Örn. 9 aralık 2023): ")
    parcalanmis_tarih = kullanici_tarihi.lower().split()  # Tüm harfleri küçült ve parçala
    # Gün, ay ve yılı parçala
    gun = parcalanmis_tarih[0].zfill(2)  # Tek haneli günler için başına 0 ekle
    ay = ay_karsiliklari.get(parcalanmis_tarih[1], "")  # Girilen ayı karşılığına dönüştür
    yil = parcalanmis_tarih[2]

    gun_td_selector = '#traditionalSearch > div.col-lg-11.col-md-12.pr-1 > div:nth-child(1) > div > div.col-lg-4.col-sm-12.col-12.pl-3.pl-md-0 > div > div.col-md-4.col-6.datepicker-box.where-date-turn.search-col > div > div > button > table > tbody > tr > td.tdday'
    ay_yil_td_selector = '#traditionalSearch > div.col-lg-11.col-md-12.pr-1 > div:nth-child(1) > div > div.col-lg-4.col-sm-12.col-12.pl-3.pl-md-0 > div > div.col-md-4.col-6.datepicker-box.where-date-turn.search-col > div > div > button > table > tbody > tr > td:nth-child(2)'

    # Gün bilgisini belirtilen <td> etiketine yerleştirin
    driver.find_element(By.CSS_SELECTOR, gun_td_selector).send_keys(gun)

    # Ay ve yıl bilgilerini uygun formatta birleştirin (Ara 2023)
    ay_yil_birlesik = f"{ay} {yil}"

    # Ay ve yıl bilgisini belirtilen <td> etiketine yerleştirin
    driver.find_element(By.CSS_SELECTOR, ay_yil_td_selector).send_keys(ay_yil_birlesik)
'''

def tarih_format_donusumu(girilen_tarih):
    # Türkçe ay isimleri ve karşılık gelecek numaraları bir sözlükte tutalım
    ay_isimleri = {
        "ocak": "01",
        "şubat": "02",
        "mart": "03",
        "nisan": "04",
        "mayıs": "05",
        "haziran": "06",
        "temmuz": "07",
        "ağustos": "08",
        "eylül": "09",
        "ekim": "10",
        "kasım": "11",
        "aralık": "12"
    }

    # Kullanıcının girdiği tarihte ay isimleri varsa, bu isimleri numaralara dönüştürelim
    for turkce_ay, numara in ay_isimleri.items():
        if turkce_ay in girilen_tarih:
            # Türkçe ay ismini, numarayla değiştirelim
            girilen_tarih = girilen_tarih.replace(turkce_ay, numara)

    # Türkçe ay isimlerini numaralara dönüştürdükten sonra gelen tarihi nokta ile birleştirelim
    girilen_tarih = girilen_tarih.replace(" ", ".")  # Boşlukları nokta ile değiştir
    return girilen_tarih

# Kullanıcıdan tarihi klavyeyle alın
girilen_tarih = input("Tarihi girin (örn. 7 ocak 2023): ")

# Tarih formatını dönüştürme işlemini yap
donusmus_tarih = tarih_format_donusumu(girilen_tarih)

driver.find_element('#whereDepartDate').send_keys(donusmus_tarih)


# Verileri girdikten sonra, belirli bir butona tıklayın
driver.find_element(By.CSS_SELECTOR, '#searchFormSubmit').click()

# 5 saniyelik bir bekleme süresi ekleyin
for i in range(5, 0, -1):
    print(f"{i} ", end="")
    time.sleep(1)

# Sonra belirli bir CSS seçici ile veriyi çekin ve görüntüleyin
alınan_veri = driver.find_element(By.CSS_SELECTOR, '#item-1 > td.flight-select.flight-price > div > span').text

if alınan_veri:
    print("\nAlınan Veri:")
    print(alınan_veri)
else:
    print("\nVeri bulunamadı veya istek yapılamadı.")

# Tarayıcıyı kapat
driver.quit()
