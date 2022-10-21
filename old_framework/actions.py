from pyautogui import *
import win32gui
from pynput.keyboard import Key, Controller
import keyboard
import time
import random
import pydirectinput
import win32api, win32con

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)

class WindowTriggers:
    
    def __init__ (self):
        """Constructor"""
        self._handle = None
    
    def type_key(self,key):
        print(" --> Typing the key: " + key);
        keyboard.press(key)
        time.sleep(random.uniform(0.1, 0.2));
        keyboard.release(key)
        time.sleep(1)

    def ns_type_key(self,key):
        print(" --> Typing the key: " + key);
        keyboard.press(key)
        time.sleep(random.uniform(0.900, 1.05));
        keyboard.release(key)
        time.sleep(random.uniform(0.7, 1));

    def click(self,x,y):
        print(" --> Left Clicking at: X:"+x + " Y:"+y);
        win32api.SetCursorPos(((int(x),int(y))));
        time.sleep(random.uniform(0.7, 1));
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0);
        time.sleep(random.uniform(0.1, 0.150));
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0);
        time.sleep(random.uniform(0.6, 0.9));

    def right_click(self,x,y):
        print(" --> Right Clicking at: X:"+x + " Y:"+y);
        win32api.SetCursorPos(((int(x),int(y))));
        time.sleep(random.uniform(0.7, 1));
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0);
        time.sleep(random.uniform(0.1, 0.150));
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0);
        time.sleep(random.uniform(0.6, 0.9));