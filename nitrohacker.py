import pyautogui
import keyboard as KB
import time
import re
import os
import random as rand
#from PIL import image
from pytesseract import *
def run():
    while(1):
            pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            img = pyautogui.screenshot(region=(628,676,639,131))
            output = pytesseract.image_to_string(img)
            print(output)
            if KB.is_pressed('esc'):
                img = pyautogui.screenshot(region=(625,665,642,149))
                output = pytesseract.image_to_string(img)
                output=' '.join(output)
                print(output)
                #//output = output.split(' ')

                #print(i+'brake')
                #chars=split(output)
                KB.write(output)
