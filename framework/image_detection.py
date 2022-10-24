
import pyautogui
from framework.triggers import Triggers
import os

class ImageDetection:

    @staticmethod
    def detect_image(image_name):
        image = pyautogui.locateOnScreen( os.getcwd() + '\\framework\\images\\' +  image_name + '.png', confidence=0.8)
        if(image != None):
            print(" --> Found the image: " + image_name)
            x, y = pyautogui.center(image)
            return x, y
        else:
            print(" --> Could not find the image: " + image_name)
            return None

    @staticmethod
    def detect_image_object(image_name):
        image = pyautogui.locateOnScreen( os.getcwd() + '\\framework\\images\\' +  image_name + '.png', confidence=0.8)
        if(image != None):
            print(" --> Found the image: " + image_name)
            return image
        else:
            print(" --> Could not find the image: " + image_name)
            return None

    @staticmethod
    def get_image_center(image):
        x, y = pyautogui.center(image)
        return x,y

    @staticmethod
    def detect_image_and_left_click(image_name):
        image = ImageDetection.detect_image(image_name)
        if(image != None):
            print(" --> Clicking the image: " + image_name + " at X:" + str(image[0]) + " Y:" + str(image[1]))
            Triggers.click(image[0],image[1])
            return True
        else:
            return False

    @staticmethod
    def detect_image_and_right_click(image_name):
        image = ImageDetection.detect_image(image_name)
        if(image != None):
            print(" --> Right clicking the image: " + image_name + " at X:" + str(image[0]) + " Y:" + str(image[1]))
            Triggers.right_click(image[0],image[1])
            return True
        else:
            return False

    @staticmethod
    def await_detect_image(image_name, sleep_time = 0, retries = 10):
        retry_count = 0
        response = ImageDetection.detect_image(image_name)

        while(response == None):
            response = ImageDetection.detect_image(image_name)
            retry_count = retry_count + 1
            pyautogui.sleep(sleep_time)
            if(retry_count >= retries):
                break

        if response != None:
            print(" --> Image found")
        else:
            print(" --> Image not found")

        return response

    @staticmethod
    def await_detect_image_and_left_click(image_name, sleep_time = 0, retries = 10):
        response = ImageDetection.await_detect_image(image_name, sleep_time, retries)
        if(response != None):
            print(" --> Clicking the image: " + image_name + " at X:" + str(response[0]) + " Y:" + str(response[1]))
            Triggers.click(response[0],response[1])
            return True
        else:
            return False

    @staticmethod
    def await_detect_image_and_right_click(image_name, sleep_time = 0, retries = 10):
        retry_count = 0
        response = ImageDetection.await_detect_image(image_name, sleep_time, retries)
        if(response != None):
            print(" --> Clicking the image: " + image_name + " at X:" + str(response[0]) + " Y:" + str(response[1]))
            Triggers.right_click(response[0],response[1])
