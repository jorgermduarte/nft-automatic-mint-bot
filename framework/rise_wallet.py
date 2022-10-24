
from framework.image_detection import ImageDetection
from framework.triggers import Triggers
import pyautogui
import json
import os

wallet_settings = json.load( open(os.getcwd() + '\\framework\\configurations\\rise_wallet_cfg.json'))
wallet_configure_access = "chrome-extension://hbbgbephgojikajhfbomhlmmollphcad/wallet.html#/access"

class RiseWallet:

    @staticmethod
    def auto_connect():
        connected = False
        connect_button = ImageDetection.await_detect_image_and_left_click('rise_wallet/rise_wallet_connect_button')
        if(connect_button == True):
            pyautogui.sleep(1.5)
            sign_button = ImageDetection.await_detect_image_and_left_click('rise_wallet/rise_wallet_connect_sign_button')
            if(sign_button == True):
                connected = True
                print("Account connected successfully")
                pyautogui.sleep(3)

        return connected

    @staticmethod
    def auto_login(password):
        input_pw = ImageDetection.await_detect_image('rise_palavra_passe_input')

        if(input_pw != None):
            #click on the input password
            Triggers.click(input_pw[0],input_pw[1])
            Triggers.type_string(password)

            button_login = ImageDetection.await_detect_image('rise_desbloquear_button')
            if(button_login != None):
                Triggers.click(button_login[0],button_login[1])

    @staticmethod
    def configure(instance,code):
        instance.get(wallet_configure_access)
        code_input = ImageDetection.await_detect_image("rise_wallet/rise_configure_enter_code")
        if(code_input != None):
            Triggers.click(code_input[0],code_input[1])
            Triggers.type_string(code)
            enter_button = ImageDetection.await_detect_image("rise_wallet/rise_configure_enter_button")
            if(enter_button != None):
                Triggers.click(enter_button[0],enter_button[1])
                pyautogui.sleep(2)
                import_account_button = ImageDetection.await_detect_image("rise_wallet/rise_configure_import_account")
                if(import_account_button != None):
                    Triggers.click(import_account_button[0],import_account_button[1])
                    password_input = ImageDetection.await_detect_image("rise_wallet/rise_configure_enter_password")
                    if(password_input != None):
                        Triggers.click(password_input[0],password_input[1])
                        Triggers.type_string(wallet_settings["password"])
                        r_password_input = ImageDetection.await_detect_image("rise_wallet/rise_configure_enter_password_repeat")
                        if(r_password_input != None):
                            Triggers.click(r_password_input[0],r_password_input[1])
                            Triggers.type_string(wallet_settings["password"])
                            continue_button = ImageDetection.await_detect_image("rise_wallet/rise_configure_continue")
                            if(continue_button != None):
                                Triggers.click(continue_button[0],continue_button[1])
                                pyautogui.sleep(1.2)
                                input_seed_phrase = ImageDetection.await_detect_image("rise_wallet/rise_configure_first_input_seed_phrase")
                                if(input_seed_phrase != None):
                                    Triggers.click(input_seed_phrase[0],input_seed_phrase[1])
                                    seed_phrase = wallet_settings["password_list"]
                                    for i in seed_phrase:
                                        Triggers.type_string(i)
                                        pyautogui.press('tab')
                                    pyautogui.sleep(1)
                                    continue_button_2 = ImageDetection.await_detect_image("rise_wallet/rise_configure_continue")
                                    if(continue_button_2 != None):
                                        Triggers.click(continue_button_2[0],continue_button_2[1])

    @staticmethod
    def configure_main_net(instance):
        instance.get("https://google.pt")
        pyautogui.sleep(1)
        extension_icon = ImageDetection.await_detect_image("rise_wallet/rise_extension_icon")
        if(extension_icon != None):
            Triggers.click(extension_icon[0],extension_icon[1])
            rise_wallet_settings = ImageDetection.await_detect_image("rise_wallet/rise_settings")
            if(rise_wallet_settings != None):
                Triggers.click(rise_wallet_settings[0],rise_wallet_settings[1])
                general_settings = ImageDetection.await_detect_image("rise_wallet/rise_config_general")
                if(general_settings != None):
                    Triggers.click(general_settings[0],general_settings[1])
                    network_settings = ImageDetection.await_detect_image("rise_wallet/rise_config_network")
                    if(network_settings != None):
                        Triggers.click(network_settings[0],network_settings[1])
                        network_settings_node = ImageDetection.await_detect_image("rise_wallet/rise_config_network_custom_node")
                        if(network_settings_node != None):
                            Triggers.click(network_settings_node[0],network_settings_node[1])
                            node_name_input = ImageDetection.await_detect_image("rise_wallet/rise_config_network_node_name")
                            if(node_name_input != None):
                                Triggers.click(node_name_input[0],node_name_input[1])
                                Triggers.type_string(wallet_settings["network_name"])
                                node_url_input = ImageDetection.await_detect_image("rise_wallet/rise_config_network_node_url")
                                if(node_url_input != None):
                                    Triggers.click(node_url_input[0],node_url_input[1])
                                    Triggers.type_string_pyautogui(wallet_settings["network_url"])
                                    save_button = ImageDetection.await_detect_image("rise_wallet/rise_config_network_node_save_button")
                                    if(save_button != None):
                                        Triggers.click(save_button[0],save_button[1])

    @staticmethod
    def auto_approve_mint():
        return False
        #mint_approve_button