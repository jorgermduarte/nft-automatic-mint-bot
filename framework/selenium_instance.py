from copyreg import constructor
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
from framework.triggers import Triggers
from framework.image_detection import ImageDetection
import pyautogui

options = webdriver.ChromeOptions()
options.add_extension(os.getcwd() + "\\framework\\selenium_extensions\\rise-wallet.crx")
options.add_argument("lang=en-GB")
options.add_experimental_option("detach", True)

class SeleniumInstance:
    def __init__(self):
        self.initialized = False

    def initialize(self):
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.maximize_window()
        self.instance =  driver
        self.initialized = True
        pyautogui.sleep(3)
        self.pinExtensions()

    def pinExtensions(self):
        img_extensions = ImageDetection.await_detect_image('extensions')
        if(img_extensions != None):
            Triggers.click(img_extensions[0],img_extensions[1])
            img_extension_pin = ImageDetection.await_detect_image('pin_extension')
            if(img_extension_pin != None):
                Triggers.click(img_extension_pin[0],img_extension_pin[1])

    def close(self):
        self.instance.close()
