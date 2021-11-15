from pynput.mouse import Controller as mController, Listener, Button
from pynput.keyboard import Controller as kController, Listener, Key
from time import sleep

mouse = mController()
kb = kController()

# number = input("How often: ")

while True:
    mouse.position = (105, 182)
    mouse.click(Button.left)
    sleep(0.3)

    mouse.position = (1368, 486)
    sleep(0.3)
    mouse.click(Button.left)
    sleep(0.3)

    kb.type("c.koopman@carmelhengelo.nl")
    sleep(0.3)
    kb.press(Key.tab)
    sleep(0.3)
    mouse.position = (1341, 515)
    sleep(0.3)
    mouse.click(Button.left)
    sleep(0.3)
    kb.type("Huiswerk")
    sleep(0.3)

    mouse.position = (1310, 1007)
    sleep(0.3)
    mouse.click(Button.left)
    sleep(0.5)