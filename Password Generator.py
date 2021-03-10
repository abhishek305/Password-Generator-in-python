import string
import random
import pyautogui

X=pyautogui.alert("Press enter")

def generatePassword(num):
    password=""

    for n in range(num):
        x=random.randint(0,94)
        password+=string.printable[x]
        
    return password

pyautogui.alert("Your password is""  "+ generatePassword(20))
