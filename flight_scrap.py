from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
  # Kullanıcıdan web sitesi adresini al
  url = input("Web sitesi adresini girin: ")

  # Tarayıcıyı başlat
  driver = webdriver.Firefox()

  # Siteye git
  driver.get(url)

  # Kullanıcıdan "Nereden?" bilgisini al ve lowercase yaparak uygun yere yaz
  nereden = input("Ucus kodu? ").lower()
  driver.find_element(By.CSS_SELECTOR, '#searchBox').send_keys(nereden)
  '''
  # Verileri girdikten sonra, belirli bir butona tıklayın
  driver.find_element(By.CSS_SELECTOR, '#searchFormSubmit').click()
  '''#onetrust-accept-btn-handler//html body.antialiased div#onetrust-consent-sdk div#onetrust-banner-sdk.otCenterRounded.default.vertical-align-content div.ot-sdk-container div.ot-sdk-row div#onetrust-button-group-parent.ot-sdk-twelve.ot-sdk-columns div#onetrust-button-group div.banner-actions-container button#onetrust-accept-btn-handler

#Gelen sehir secicisi: #app > div > div > div.absolute.inset-x-0.top-0.z-40 > div > div > div > div.relative.flex.h-13.w-full.items-center.justify-end > div.pointer-events-auto.relative.mr-4.flex.items-center.justify-between.space-x-4.text-sm.xl\:space-x-8 > div.xx\:w-full.lg\:w-auto > div.z-search.shadow-default.absolute.w-100.rounded-lg.mt-2 > div > div > div > div.contents > div > div:nth-child(2) > div:nth-child(2) > div > div > a > div.flex.w-0.flex-1.flex-col.justify-center.space-y-0\.5.py-1.pl-2 > div > div:nth-child(1) > span
#Gidilen sehir secicisi: #app > div > div > div.absolute.inset-x-0.top-0.z-40 > div > div > div > div.relative.flex.h-13.w-full.items-center.justify-end > div.pointer-events-auto.relative.mr-4.flex.items-center.justify-between.space-x-4.text-sm.xl\:space-x-8 > div.xx\:w-full.lg\:w-auto > div.z-search.shadow-default.absolute.w-100.rounded-lg.mt-2 > div > div > div > div.contents > div > div:nth-child(2) > div:nth-child(2) > div > div > a > div.flex.w-0.flex-1.flex-col.justify-center.space-y-0\.5.py-1.pl-2 > div > div:nth-child(4) > span

  # Sonra belirli bir CSS seçici ile veriyi çekin ve görüntüleyin
  alınan_veri = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.absolute.inset-x-0.top-0.z-40 > div > div > div > div.relative.flex.h-13.w-full.items-center.justify-end > div.pointer-events-auto.relative.mr-4.flex.items-center.justify-between.space-x-4.text-sm.xl\:space-x-8 > div.xx\:w-full.lg\:w-auto > div.z-search.shadow-default.absolute.w-100.rounded-lg.mt-2 > div > div > div > div.contents > div > div:nth-child(1) > div:nth-child(2) > div > div > a > div.flex.w-0.flex-1.flex-col.justify-center.space-y-0\.5.py-1.pl-2 > div > div:nth-child(4) > span').text

  if alınan_veri:
      print("\nAlınan Veri:")
      print(alınan_veri)
  else:
      print("\nVeri bulunamadı veya istek yapılamadı.")

except NoSuchElementException:
  print("\nVeri bulunamadı veya istek yapılamadı. Element bulunamadı.")

except Exception as e:
    print("\nBeklenmeyen bir hata oluştu:", str(e))

finally:
    # Tarayıcıyı kapat
    driver.quit()
