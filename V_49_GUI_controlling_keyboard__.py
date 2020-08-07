import pyautogui
#pyautogui.click(100,100); pyautogui.typewrite('Hello world' , interval = 2 )# it will click on coordinate 100,100 then start to write , incase you change the courser to another page , then it will continue writing.

#pyautogui.tHeypewrite(['a', 'b', 'left','left','X','Y'] , interval = 2 ) # press a  , b__it will go left __left__then type XY.

pyautogui.KEYBOARD_KEYS # buttons that you can use
print(pyautogui.KEYBOARD_KEYS)

pyautogui.press('F1') # to press F1

pyautogui.hotkey('ctrl','o') # to press multi keys

# you can use Selenum with this.
