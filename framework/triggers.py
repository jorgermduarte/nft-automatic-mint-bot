import os
from pyautogui import *
import time
import random
import keyboard
import win32api
import win32con
import pyautogui

class Triggers:

    @staticmethod
    def sleepy_type_key(key, sleep_time = 0.400):
        print(" --> Sleepy typing the key: " + key)
        keyboard.press(key)
        time.sleep(random.uniform(0.100, 0.200))
        keyboard.release(key)
        time.sleep(sleep_time)

    @staticmethod
    def type_key(key,sleep_min_time = 0.010, sleep_max_time = 0.020):
        print(" --> Typing the key: " + key)
        keyboard.press(key)
        time.sleep(random.uniform(sleep_min_time, sleep_max_time))
        keyboard.release(key)

    def type_string_pyautogui(value, interval= 0.05):
        pyautogui.write(value,interval=interval)

    @staticmethod
    def type_string(string_value,sleep_min_time = 0.010, sleep_max_time = 0.020):
        for element in range(0, len(string_value)):
            Triggers.type_key(string_value[element],sleep_min_time, sleep_max_time)

    @staticmethod
    def click(x,y):
        print(" --> Left Clicking at: X:"+ str(x) + " Y:"+ str(y))
        win32api.SetCursorPos(((int(x),int(y))))
        time.sleep(random.uniform(0.05, 0.15))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(random.uniform(0.05, 0.15))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(random.uniform(0.05, 0.15))

    @staticmethod
    def right_click(x,y):
        print(" --> Right Clicking at: X:"+ str(x) + " Y:"+ str(y))
        win32api.SetCursorPos((x,y))
        time.sleep(random.uniform(0.05, 0.15))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(random.uniform(0.05, 0.15))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        time.sleep(random.uniform(0.05, 0.15))
