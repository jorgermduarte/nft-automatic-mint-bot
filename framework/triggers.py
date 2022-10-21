from pyautogui import *
import time
import random
import keyboard

class Triggers:
    @staticmethod
    def sleepy_type_key(key):
        print(" --> Typing the key: " + key);
        keyboard.press(key)
        time.sleep(random.uniform(0.1, 0.2));
        keyboard.release(key)
        time.sleep(1)

    @staticmethod
    def type_key(key):
        print(" --> Typing the key: " + key);
        keyboard.press(key)
        time.sleep(random.uniform(0.050, 0.075));
        keyboard.release(key)
        time.sleep(random.uniform(0.050, 0.100));

    @staticmethod
    def click(x,y):
        print(" --> Left Clicking at: X:"+x + " Y:"+y);
        #win32api.SetCursorPos(((int(x),int(y))));
        time.sleep(random.uniform(0.05, 0.15));
        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0);
        time.sleep(random.uniform(0.05, 0.15));
        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0);
        time.sleep(random.uniform(0.05, 0.15));

    @staticmethod
    def right_click(x,y):
        print(" --> Right Clicking at: X:"+x + " Y:"+y);
        #win32api.SetCursorPos(((int(x),int(y))));
        time.sleep(random.uniform(0.05, 0.15));
        #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0);
        time.sleep(random.uniform(0.05, 0.15));
        #win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0);
        time.sleep(random.uniform(0.05, 0.15));