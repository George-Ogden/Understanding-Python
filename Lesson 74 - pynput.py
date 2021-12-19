
from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.keyboard import Key
import time

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()
print(mouse_controller.position)

for i in range(100):
    mouse_controller.move(5,-5)
    time.sleep(0.01)

mouse_controller.click(Button.right)
mouse_controller.press(Button.left)

def on_move(x,y):pass

def on_click(x,y,button,pressed):
    print((x,y),button,pressed)
    if button == Button.right:
        return False

def on_scroll(x,y,dx,dy):
    print((dx,dy))

with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll
    ) as mouse_listener:
    mouse_listener.join()

with keyboard_controller.pressed(Key.shift):
    keyboard_controller.press("a")
    keyboard_controller.press("b")
keyboard_controller.press("A")

def on_press(key):
    print(key)

def on_release(key):
    if key == Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release
    ) as keyboard_listener:
    keyboard_listener.join()