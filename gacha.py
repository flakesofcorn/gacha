import ctypes
import time
import keyboard
import pyautogui
import threading
screen_width, screen_height = pyautogui.size()

def is_within_main_screen(x, y):
    """
    Check if the given coordinates are within the main screen bounds.

    Args:
        x (int): X-coordinate to check.
        y (int): Y-coordinate to check.

    Returns:
        bool: True if the coordinates are within the main screen, False otherwise.
    """
    return 0 <= x < screen_width and 0 <= y < screen_height

# ctypes structure for input simulation
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def move_mouse(x, y):
    """
    Move the mouse cursor to absolute screen coordinates (Direct Input).

    Args:
        x (int): X-coordinate to move to (screen-based).
        y (int): Y-coordinate to move to (screen-based).
    """
    ctypes.windll.user32.SetCursorPos(x, y)
    print(f"Mouse moved to ({x}, {y}).")

def move_mouse_relative(x_offset, y_offset):

    # Get the current mouse position
    pt = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    
    # Calculate new position
    new_x = pt.x + x_offset
    new_y = pt.y + y_offset
    
    # Move the cursor to the new position
    move_mouse(new_x, new_y)

    
def berry_station( ):
    
    time.sleep(2)
    keyboard.press_and_release('f')
    time.sleep(2)
    move_mouse(413, 193)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    keyboard.press_and_release('f')
    
    
    time.sleep(2)
    keyboard.press('e')
    time.sleep(0.5)
    move_mouse(1109, 385)
    time.sleep(0.1)
    keyboard.release('e')
    time.sleep(2)
    
    keyboard.press_and_release("f")
    time.sleep(2)
    move_mouse(1329, 201)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.7)
    keyboard.press_and_release("s")
    keyboard.press_and_release("e")
    keyboard.press_and_release("e")
    keyboard.press_and_release("d")
    time.sleep(0.5)
    move_mouse(1432, 201)
    pyautogui.click()
    time.sleep(1)
    move_mouse(1246, 385)
    time.sleep(0.7)
    pyautogui.click()
    keyboard.press_and_release("t")
    time.sleep(0.2)
    move_mouse(312, 276)
    time.sleep(0.7)
    pyautogui.click()
    keyboard.press_and_release("t")
    time.sleep(0.7)
    keyboard.press_and_release("esc")
    
    time.sleep(2)
    keyboard.press('e')
    time.sleep(0.5)
    move_mouse(1109, 385)
    time.sleep(0.1)
    keyboard.release('e')
    time.sleep(2)
    1
    keyboard.press_and_release("f")
    time.sleep(2)
    move_mouse(1329, 201)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.7)
    keyboard.press_and_release("s")
    keyboard.press_and_release("e")
    keyboard.press_and_release("e")
    keyboard.press_and_release("d")
    time.sleep(0.5)
    move_mouse(1432, 201)
    pyautogui.click()
    time.sleep(0.5)
    move_mouse(1246, 385)
    time.sleep(0.7)
    pyautogui.click()
    keyboard.press_and_release("t")
    time.sleep(0.2)
    move_mouse(312, 276)
    time.sleep(0.7)
    pyautogui.click()
    keyboard.press_and_release("t")
    time.sleep(0.7)
    keyboard.press_and_release("esc")
    
    
def gacha_station1():
    time.sleep(1)
    keyboard.press('right')
    time.sleep(1)
    keyboard.release('right')
    time.sleep(0.5)
    keyboard.press_and_release('f')
    time.sleep(1)
    move_mouse(413, 191)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    keyboard.press('esc')
    
def gacha_station2():
    time.sleep(1)
    keyboard.press('right')
    time.sleep(3)
    keyboard.release('right')
    time.sleep(0.5)
    keyboard.press_and_release('f')
    time.sleep(2)
    move_mouse(413, 191)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    keyboard.press('esc')
    

def chair2():
    time.sleep(1)
    keyboard.press('up')
    time.sleep(0.5)
    keyboard.release('up')
    time.sleep(0.8)
    keyboard.press('left')
    time.sleep(0.5)
    keyboard.release('left')
    time.sleep(0.5)
    keyboard.press_and_release('e')
    
def chair_after_pod():
    time.sleep(1)
    keyboard.press_and_release('e')
    time.sleep(1)
    keyboard.press_and_release('e')
    time.sleep(1)
      
def pod():
    time.sleep(0.5)
    keyboard.press('up')
    time.sleep(4)
    keyboard.release('up')
    time.sleep(0.5)
    
    keyboard.press('e')
    time.sleep(0.5)
    move_mouse(1109, 385)
    time.sleep(0.1)
    keyboard.release('e')
    time.sleep(5)
    keyboard.press_and_release('e')
    
    
def TPH():
    time.sleep(1)
    keyboard.press('down')
    time.sleep(2.3)
    keyboard.release('down')
    time.sleep(0.5)
    keyboard.press_and_release('e')
    time.sleep(1.5)
    move_mouse(406, 970)
    time.sleep(0.7)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.7)
    keyboard.write('<<')
    time.sleep(0.7)
    move_mouse(390, 226)
    time.sleep(0.7)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.7)
    move_mouse(1645, 957)
    time.sleep(0.7)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(1.5) 
        
def TP(i):
    time.sleep(1)
    keyboard.press('down')
    time.sleep(2.3)
    keyboard.release('down')
    time.sleep(0.5)
    keyboard.press_and_release('e')
    time.sleep(1.5)
    move_mouse(406, 970)
    time.sleep(0.7)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.7)
    keyboard.write(i)
    time.sleep(0.7)
    move_mouse(390, 226)
    time.sleep(0.7)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(0.7)
    move_mouse(1645, 957)
    time.sleep(0.7)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(1.5)
 

def level_cam():
    time.sleep(1)
    keyboard.press('up')
    time.sleep(1.8)
    keyboard.release('up')
    time.sleep(0.5)

def trough():
    time.sleep(4)
    keyboard.press_and_release('f')
    time.sleep(2)
    move_mouse(1434, 197)
    time.sleep(2)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(2)
    keyboard.press_and_release('esc')
    
def start():
    time.sleep(2)
    keyboard.press('right')
    time.sleep(2)
    keyboard.release('right')


def feed(i):
    chair_after_pod()
    start()
    berry_station()
    TP(i)
    level_cam()
    gacha_station1()
    TPH()
    time.sleep(1)
    level_cam()
    time.sleep(1)
    berry_station()
        

    TP(i)
    level_cam()
    gacha_station2()
    TPH()
    pod()
    time.sleep(1)

def automate_process():
    
    if is_within_main_screen(10, 10):
        move_mouse(10, 10)
        pyautogui.click()
        keyboard.press_and_release('E')
    else: 
        exit()
    while True:
        trough()
        for i in range(1, 31):
            string_variable = f"{i:02}"  # Format the number with leading zeros
            feed_thread = threading.Thread(target=feed, args=(string_variable,))
            feed_thread.start()
            feed_thread.join()
            if i % 5 == 0:
                time.sleep(10)
                
        time.sleep(100)

 



