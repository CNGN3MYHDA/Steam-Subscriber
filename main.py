import time
import pickle

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def subscribe_addons(urls_list):
    try:
        driver = webdriver.Chrome(
            service=Service(r"E:\PyCharm Community Edition 2022.3.3\Projects\subs\driver\chromedriver.exe")
        )

        print("[!] Please, authorize!")
        time.sleep(3)
        driver.get(r"https://steamcommunity.com")
        input("Enter something after authorization to continue: ")

        for url in urls_list:
            print(f"[!] Reading {url.strip()}...")
            driver.get(url)

            sub_button = driver.find_element(by=By.ID, value="SubscribeItemBtn")
            btn_class = sub_button.find_element(by=By.ID, value="SubscribeItemOptionAdd").get_attribute("class")
            if "selected" not in btn_class:
                print("[×] Already subscribed\n")
            else:
                sub_button.click()
                print(f"[✓] Subscribed!\n")

        print(f"[✓] Success!")
    except selenium.common.exceptions.NoSuchWindowException:
        print(f"[×] Damn... Where is my window?")
    except Exception as ex:
        print(f"[×] Wow! It's a problem! Exception:\n\t{ex}")


def main():
    print("[!] Starting...")
    try:
        print("[!] Reading addons.txt...")
        with open("addons.txt", "r") as addons:
            addons = addons.readlines()
            subscribe_addons(addons)

    except FileNotFoundError:
        print(f"[×] Damn... File 'addons.txt' isn't exists. Create it!")
    except Exception as ex:
        print(f"[×] Wow! It's a problem! Exception:\n\t{ex}")


if __name__ == "__main__":
    main()
    print("[!] End of program")
    while True:
        pass
