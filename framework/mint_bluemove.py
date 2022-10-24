import json
import os
import pyautogui
from framework.image_detection import ImageDetection
from framework.triggers import Triggers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from framework.rise_wallet import RiseWallet
import threading

wallet_settings = json.load( open(os.getcwd() + '\\framework\\configurations\\rise_wallet_cfg.json'))

class MintBlueMove:

    @staticmethod
    def connect_wallet(driver):
        print("connecting wallet to the website")
        pyautogui.sleep(2)
        driver.find_element(By.LINK_TEXT, "Connect Wallet").click()
        pyautogui.sleep(2)
        driver.find_element(By.CSS_SELECTOR, ".relative:nth-child(4) .ml-4").click()
        RiseWallet.auto_connect()
        pyautogui.sleep(2)

    @staticmethod
    def try_mint(driver):
        try:
            #mint_button = driver.find_element(By.XPATH,"//*[contains(text(),'Mint')]").click()
            mint_button = driver.find_element(By.XPATH,"//*[text()='Mint']").click()
            print('mint button detected and clicked!')
            pyautogui.sleep(1)
            MintBlueMove.try_mint(driver)
        except:
            print('something went wrong, retrying to find the mint button')
            pyautogui.sleep(0.3)
            MintBlueMove.try_mint(driver)

    @staticmethod
    def try_auto_payment():
        approve_transaction = ImageDetection.await_detect_image('rise_wallet/mint_approve_button')
        if(approve_transaction != None):
            Triggers.click(approve_transaction[0],approve_transaction[1])
            pyautogui.sleep(0.1)
            MintBlueMove.try_auto_payment()
        else:
            pyautogui.sleep(0.1)
            MintBlueMove.try_auto_payment()

    @staticmethod
    def start(Instance):
        Instance.get(wallet_settings["target_website"])
        MintBlueMove.connect_wallet(Instance)
        Instance.get(wallet_settings["target_website_mint"])
        pyautogui.sleep(1)
        # now since we are at the mint website, we are going to start two threads differently

        # the first is the one that constantly try to mint the page
        auto_mint = threading.Thread(target=MintBlueMove.try_mint, args=(Instance,))
        # the second is the auto payment thread
        auto_payment = threading.Thread(target=MintBlueMove.try_auto_payment, args=())

        auto_mint.start()
        auto_payment.start()