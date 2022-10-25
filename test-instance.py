from framework.selenium_instance import SeleniumInstance
from framework.rise_wallet import RiseWallet
from framework.mint_bluemove import MintBlueMove
from framework.mint_aptos import MintAptos
import pyautogui
import json
import os

wallet_settings = json.load( open(os.getcwd() + '\\framework\\configurations\\rise_wallet_cfg.json'))

class TestInstance:

    def __init__(self):
        self.initialized = False

    def initialize(self):
        Instance = SeleniumInstance()
        Instance.initialize()
        RiseWallet.configure(Instance.instance,"RISE")
        pyautogui.sleep(2)
        #RiseWallet.configure_main_net(Instance.instance)
        #pyautogui.sleep(2)


bot = TestInstance()
bot.initialize()