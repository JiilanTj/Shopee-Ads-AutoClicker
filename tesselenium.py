import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from prettytable import PrettyTable
from colorama import Fore, Style

# Inisialisasi warna
green = Fore.GREEN
reset = Style.RESET_ALL

options = Options()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Tampilan
header = f"{' Tools Name ':^20} | {' Version ':^10} | {' Creator ':^20} | {' License ':^20} | {' Note ':^30}"
header = f"{green}{header}{reset}"
table = PrettyTable([" Tools Name ", " Version ", " Creator ", " License ", " Note "])
table.align = 'l'
table.add_row(["Shopee Auto Clicker", "1.03 Alpha", "Jiilan N. Tanjung", "Tidak diperjual belikan ulang",
                "For educational purposes only, all misuse of this tool is responsible for the user and not the "
                "creator"])

print(table)

# Meminta pengguna untuk memasukkan link toko Shopee
shop_link = input("Masukkan link toko Shopee: ")

# Memeriksa apakah link toko Shopee aktif
response = requests.get(shop_link)
if response.status_code == 200:
    print(f"{green}Toko teridentifikasi{reset}")

    # Meminta pengguna untuk memasukkan kata kunci
    search_keyword = input("Masukkan kata kunci: ")

    # Meminta pengguna untuk memasukkan jumlah pengulangan
    num_iterations = int(input("Masukkan jumlah Spam: "))



    new_num_iterations = str(num_iterations)

    for _ in range(num_iterations):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Buka Shopee
        driver.get('https://shopee.co.id/')

        # Temukan elemen input pencarian dengan XPath yang telah Anda berikan
        search = driver.find_element(by=By.XPATH,
                                     value='//*[@id="main"]/div/header/div[2]/div/div[1]/form/div/div[1]/input')

        # Masukkan kata kunci yang dimasukkan pengguna ke dalam input pencarian
        search.send_keys(search_keyword)

        # Tekan tombol Enter
        search.send_keys(Keys.RETURN)

        # Tunggu beberapa saat untuk hasil pencarian muncul
        time.sleep(1.5)

        # Tutup browser
        driver.close()
else:
    print(f"{Fore.RED}Toko tidak ada{Style.RESET_ALL}")
