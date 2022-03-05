#import pymeow
from decimal import Rounded
from tkinter import VERTICAL
from traceback import print_tb
import keyboard
import mouse
import pyautogui #not needed rn but might be of use later
import random as rd
import time
import ReadWriteMemory as rwm
from PIL import Image, ImageGrab
import pytesseract
from time import sleep

#the Ai lib
#import keras 
#https://faroit.com/keras-docs/1.2.0/
#https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

'''
To do:
    Train AI
        - make sure to restart the map if AI dies
        - just takes time
    
    Make a array with the cords of every placed monkey, this allows them to be upgraded later.
    Also remember the past upgrades

    Get a list of prices, for every upgrade

    Read: 
        Hp counter
        Check for death if so restart

    Feed values to AI
        - prob just make a main function that has the smaller functions with some values passed in to it
'''

'''
Extra features:
    fix the hotfixes:
        - The alt-tab to game function, could prob use a lib to select the exe program or smt
        - allow the program to work with different screen sizes
'''



#pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\tesseract.exe'  # your path may be different
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # your path may be different


#https://noob3xploiter.medium.com/game-hacking-with-python-and-cheat-engine-5000369e27b9
#https://www.youtube.com/watch?v=QoEMoSbGvbM&t=9s

#if money goes down = tower suscesfull placed

#https://github.com/qb-0/PyMeow/blob/master/cheatsheet.txt

#https://stackoverflow.com/questions/63442491/get-data-at-address-from-cheat-engine-with-python
#maybe a different way of getting the money,lives and round counters out of the RAM

#https://pypi.org/project/ReadWriteMemory/
#Ram lib


#The hotkeys for every tower
monkeys = {
    "DART": "Q",
    "BOOMERANG": "W",
    "BOMB": "E",
    "TACK": "R",
    "ICE": "T",
    "GLUE": "Y",
    "SNIPER": "Z",
    "SUBMARINE": "X",
    "BUCCANEER": "C",
    "ACE": "V",
    "HELI": "B",
    "MORTAR": "N",
    "DARTLING": "M",
    "WIZARD": "A",
    "SUPER": "S",
    "NINJA": "D",
    "ALCHEMIST": "F",
    "DRUID": "G",
    "BANANA": "H",
    "ENGINEER": "L",
    "SPIKE": "J",
    "VILLAGE": "K",
    "HERO": "U"
}

'''
>>> pyautogui.size()  # current screen resolution width and height
(1920, 1080)
'''
#might help with making the AI adapt to different screen sizes
screensize = 1920, 1080
run = True

#def Brain(Round, Other_Towers, money)




































#this is a hot fix to select the game
def Tab_To_Game():
    mouse.move(0, 0)
    mouse.click("left")


#this hero is needed to give the bomb shooters camo
#check if money goes down cuz that == tower is placed
def Etienne():
    mouse.move(rd.randrange(1500),rd.randrange(1080))
    time.sleep(0.3)
    keyboard.press_and_release("U")
    mouse.click("left")

#some old code
#this sould be removed or commented out
def Random_Tower():
    mouse.move(rd.randrange(1500),rd.randrange(1080))
    time.sleep(0.3)
    keyboard.press_and_release("E")
    mouse.click("left")


#needs a brain
def Upgrade_Towers():
    keyboard.press_and_release(",") #upgrade path 1
    keyboard.press_and_release(".") #upgrade path 2
    keyboard.press_and_release("/") #upgrade path 3


#needs a brain
def Place_To(Tower_X,Tower_Y): #X is horizontal, Y is vertical
    mouse.move(Tower_X,Tower_Y)
    time.sleep(0.3)
    keyboard.press_and_release("E")
    mouse.click("left")



#dont change these values, its a fucking pain in the ass to get them right
#this only works on my pc I think, same as the Tab_To_Game function
#needs to be dinamic, not sure tho
def Get_Money_Count():
    Money_Img = ImageGrab.grab(bbox =(338, 0, 610, 80))
    Money_Count = pytesseract.image_to_string(Money_Img, config="--psm 13")
    print(''.join(c for c in Money_Count if c.isdigit()))
    Money_Img.show()

def Get_Round_Count():
    Round_Img = ImageGrab.grab(bbox =(1350, 0, 1490, 100))
    Round_Count = pytesseract.image_to_string(Round_Img, config="--psm 7")
    print(''.join(c for c in Round_Count if c.isdigit()))
    print(Round_Count)
    Round_Img.show()

def Get_Lives_Count():
    Lives_Img = ImageGrab.grab(bbox =(120, 0, 250, 80))
    Lives_Count = pytesseract.image_to_string(Lives_Img, config="--psm 13")
    print(''.join(c for c in Lives_Count if c.isdigit()))
    Lives_Img.show()

def Victory():
    Victory_Img = ImageGrab.grab(bbox =(700, 110, 1200, 240))
    Victory_string = pytesseract.image_to_string(Victory_Img, config="--psm 13")

    print(Victory_string)
    if Victory == ("VICTORY"):
        print("Victory")
    Victory_Img.show()

def Defeat():
    Defeat_Img = ImageGrab.grab(bbox=(730,290,1200,400))
    Defeat_string = pytesseract.image_to_string(Defeat_Img, config="--psm 13")
    print(Defeat_string)
    Defeat_Img.show()
    if Defeat_string == ('DEFEAT:'):
        print("works")

#Get_Money_Count()
#Get_Round_Count()
#Get_Lives_Count()
#Victory()
Defeat()



#prob needs data
#aka feed this function the data from the brain
#def Decisions():
    #if live counter == 0: #this kills the program if the game is lost, prob needs to change to just reset the level
        #break
    #if 

#def main():
    #Decisions()
    #while run == True:
    #if keyboard.is_pressed('esc'):
        #run = False

'''
Tab_To_Game()
Etienne()
keyboard.press_and_release('space')
time.sleep(0.3)
keyboard.press_and_release('space')
while run == True:
    try:
        Random_Tower()
        Upgrade_Towers()
    exept keyboard.is_pressed('esc'):
        run = False
'''

"""
pyautogui.keyDown('alt')
sleep(.5)
title=pyautogui.getActiveWindowTitle()
print(title)
while True:
    pyautogui.press('tab')
    title=pyautogui.getActiveWindowTitle()
    print(title)
    sleep(.2)
    #Match the predefined title
    # if matches:
    #   pg.keyUp('alt')
    #   try:
    #       (i,j) = pg.locateCenterOnScreen('./ok.png', confidence =0.5)
    #       pg.click(i,j)
  
    #       pg.alert("Done!")
    #       print("done")
    #       break
    # else:
    #   pass
"""