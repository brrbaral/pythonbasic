import pyautogui
import time
#pyautogui.click(150,150)
#pyautogui.dragto(300,500,duration=20)

time.sleep(15)
pyautogui.moveTo(300,300,duration=1)
pyautogui.dragRel(300,0,duration=2)
pyautogui.dragRel(0,300,duration=2)
pyautogui.dragRel(-300,0,duration=2)
pyautogui.dragRel(0,-300,duration=2)
