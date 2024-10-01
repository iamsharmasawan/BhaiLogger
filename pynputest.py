from pynput.mouse import Controller
from pynput.keyboard import Controller
# these two are used to send data

from pynput.keyboard import Listener
from pynput.mouse import Listener


def writetofile(x,y):
    print('Position of Current mouse {0}' .format((x,y)))
with Listener(on_move=writetofile) as l:
    l.join()



# def controlMouse():
#     mouse = Controller()
#     mouse.position = (10,20) #Left to right and top to bottom
# # controlMouse()
#
# def controKeyboard():
#     keyboard = Controller()
#     keyboard.type("I am a Devil")
# controKeyboard()
# Controlling Your Mouse
# Listening to Your Mouse
# Controlling Your KeyBoard ((I am a Devil))
# Listening to your KeyBoard - Using in our Project BhaiLogger



