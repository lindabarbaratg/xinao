from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
import string
import random

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "gaslagi"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


with open("data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        kw = line[0]

        def web_driver():
            options = webdriver.ChromeOptions()
            options.add_argument("--verbose")
            # options.add_argument('--no-sandbox')
            # options.add_argument('--headless')
            options.add_argument("--disable-gpu")
            # options.add_argument("--window-size=1920, 1200")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)
            return driver

        driver = web_driver()
        driver.maximize_window()

        email ='hermanpentol'
        password ='Qwerty12ba'

        try:

            nama_modif = kw.replace(" ", "-")
            gmail = f"{nama_modif}-onlyfans-vidx{random_string(6)}@gmail.com"
            slug = f"{nama_modif}-telegram-chanel-x{random_string(6)}"

          
            
            judul = f"*# {kw} -Telegram Catalog"
            
           # Login
            driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(email)
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()
            time.sleep(5)

            modif_kata = kw.replace(' ', '_')
            kw = f'{kw} Onlyfans Leaked - Update Files ++ Download'

            konten = f'''
            17 minutes ago - Access {kw} Onlyfans Leaked content & files Update.

            LINK ⏩⏩ https://clipsmu.com/{modif_kata}

            2025 Updated! Today, you'll be able to download and preview all content from {kw} in just a few clicks.
            '''

            

            video_path = os.path.abspath("video/video.mp4")
            
            driver.get("https://old.bitchute.com/channel/")
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, ".svg-inline--fa.fa-upload.fa-2x").click()
            time.sleep(5)
            driver.find_element(By.CSS_SELECTOR, "input[name='videoInput']").send_keys(video_path)
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "input[type='title']").send_keys(kw)
            time.sleep(20)
            driver.find_element(By.CSS_SELECTOR,"button[id='thumbnailButton']").click()
            time.sleep(15)
            driver.find_element(By.CSS_SELECTOR, "textarea[id='description']").send_keys(konten)
            time.sleep(5)
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(7)
            print("Berhasil Upload : "+kw)

            # response = (
            #     supabase.table(SUPABASE_TABLE_NAME)
            #     .insert({"result": driver.current_url})
            #     .execute()
            # )

            print(f"SUKSES CREATE: {kw}")

            time.sleep(5)
            driver.close()
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")
            driver.close()
