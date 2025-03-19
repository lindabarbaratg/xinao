from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from supabase import create_client, Client
from threading import Thread, Event
import time
import csv
import string
import random
import sys
import os

from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    wait,
    FIRST_EXCEPTION,
)

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "dos2"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

email = 'hermanpentol'
password = 'Qwerty12ba'


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


def load_data(start_data, end_data):

    script_dir = os.path.dirname(os.path.realpath("__file__"))
    data_file = os.path.join(script_dir, "x.csv")

    data_account = []

    with open(data_file) as csv_data_file:
        data_account = list(csv.reader(csv_data_file, delimiter=","))

    data_account = data_account[int(start_data) : int(end_data)]

    return data_account


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


def run_bot(data_account, recover=1):
    kw = data_account[0]
    modif = kw.replace(" ","_")
    driver = web_driver()
    driver.maximize_window()

  

    try:

       

        driver.get("https://old.bitchute.com/channel/")
        time.sleep(3)

        # Login
        driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys(email)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()
        time.sleep(5)

        modif_kata = kw.replace(' ', '_')
        judul = f'{kw} Onlyfans Leaked - Update Files ++ Download ({random_string(5)})'

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
        driver.find_element(By.CSS_SELECTOR, "input[type='title']").send_keys(judul)
        time.sleep(20)
        driver.find_element(By.CSS_SELECTOR,"button[id='thumbnailButton']").click()
        time.sleep(15)
        driver.find_element(By.CSS_SELECTOR, "textarea[id='description']").send_keys(konten)
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(7)
        

        print(f"SUKSES CREATE: {kw}", file=sys.__stderr__)

        time.sleep(5)
        driver.close()
    except Exception as e:
        if recover == 0:
            print(
                f"TERJADI ERROR: ${e}",
                file=sys.__stderr__,
            )
            #driver.close()
            return e

        run_bot(data_account, recover - 1)


def main():

    if len(sys.argv) < 3:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    start_data = int(sys.argv[1])
    end_data = int(sys.argv[2])

    workers = 1

    if not start_data and not end_data:
        print('Params require "node run.js 0 5"')
        os._exit(1)

    data = load_data(start_data, end_data)

    futures = []
    line_count = 0
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for index in range(start_data + 1, end_data + 1):
            try:
                futures.append(
                    executor.submit(
                        run_bot,
                        data[line_count],
                    )
                )
            except:
                pass
            line_count += 1

    wait(futures, return_when=FIRST_EXCEPTION)


if __name__ == "__main__":
    main()
