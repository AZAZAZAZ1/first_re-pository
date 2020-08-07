import pyautogui
#pyautogui.size()
#print(pyautogui.size()) # it will give the screen resolution  wedith , hight __pixels__

#pyautogui.position() # it will give you the mouse courser position_it can be used to get the button coordinates__result  :  Point(x=1020, y=355)
#print(pyautogui.position())

#pyautogui.moveTo(0,0, duration =4) # it will move the mouse to the (0,0) coordinate within 4 second

pyautogui.moveRel(233,122, duration =4) # move relative to the current postion 233 pixels in x (right) and 233 in y (down)  

pyautogui.click (x=1020, y=355) # to click in button after gettingthe button position
pyautogui.click() # you can put the coursee on the putton __run the comand by enter__it will click it.

pyautogui.doubleClick (x=1020, y=355) # double clikc

#pyautogui.rightClick()
#pyautogui.middleClick()

# Note: you can get real time mouse position by: go to Cmd__ >>py - 3.7 __>>pyautogui.displayMousePosition()__# click Crtl to quit.
# then you can get the corrdinate of the buttons that you need to click quickly .

