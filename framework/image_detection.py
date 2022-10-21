from pyautogui import *

from triggers import Triggers

class ImageDetection:

    @staticmethod
    def detect_image(image_name):
        image = pyautoguy.locateOnScreen( 'images/' +  image_name + '.png', confidence=0.8):
        if(image != None):
            print(" --> Found the image: " + image_name)
            x, y = pyautogui.center(image)
            return x, y
        else:
            print(" --> Could not find the image: " + image_name)
            return None

    @staticmethod
    def detect_image_and_click(image_name):
        image = ImageDetection.detect_image(image_name)
        if(image != None):
            print(" --> Clicking the image: " + image_name + " at X:" + image[0] + " Y:" + image[1])
            Triggers.click(image[0],image[1])
            return True
        else:
            return False

    @staticmethod
    def detect_image_and_right_click(image_name):
        image = ImageDetection.detect_image(image_name)
        if(image != None):
            print(" --> Right clicking the image: " + image_name + " at X:" + image[0] + " Y:" + image[1])
            Triggers.right_click(image[0],image[1])
            return True
        else:
            return False
