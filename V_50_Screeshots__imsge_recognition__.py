import pyautogui

#pyautogui.screenshot('C:\\Users\\E.H.PAUE\\python lessons\\test.png') # it will take screen shot and save it

print(pyautogui.screenshot())

 #you can refer to chapter 17 for pilow image.

pyautogui.locateOnScreen('C:\\Users\\E.H.PAUE\\python lessons\\calc_7.png')# it will compair waht is in the picture and find it in the screen


print(pyautogui.locateOnScreen('C:\\Users\\E.H.PAUE\\python lessons\\calc_7.png'))


print (pyautogui.locateCenterOnScreen('C:\\Users\\E.H.PAUE\\python lessons\\calc_7.png'))# it will compair waht is in the picture and find it in the screen but in the centre

# in the above you will get None because the pixils are not 100% identical between the picture and the screen.
