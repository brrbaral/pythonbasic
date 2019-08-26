import pyautogui

#SHOW THE SIZE OF THE SECREEN(SCREEN REOLUTION)
print(pyautogui.size())

#MOVE THE MOUSE AUTOMATICALLY
pyautogui.moveTo(100,100, duration=10)

#MOVE THE MOUSE RELATIVE TO ITS PREVIOUS POSITION
pyautogui.moveRel(0,500,duration=2)

#TO KNOW THE CURRENT POSITION OF A MOUSE POINTER
print(pyautogui.position())