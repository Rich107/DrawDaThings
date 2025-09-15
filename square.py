import pyautogui
import time

pyautogui.PAUSE = 0

# Wait a few seconds to give you time to switch to the Slack window
time.sleep(0)

# Get the current mouse position
center_x, center_y = pyautogui.position()

# Draw the square with the same diameter as the circle (200 pixels)
square_size = 200

# Draw top line
pyautogui.moveTo(center_x - square_size//2, center_y - square_size//2)
pyautogui.mouseDown()
pyautogui.moveTo(center_x + square_size//2, center_y - square_size//2)

# Draw right line
pyautogui.moveTo(center_x + square_size//2, center_y + square_size//2)

# Draw bottom line
pyautogui.moveTo(center_x - square_size//2, center_y + square_size//2)

# Draw left line
pyautogui.moveTo(center_x - square_size//2, center_y - square_size//2)

pyautogui.PAUSE = 0.1
pyautogui.mouseUp()

print("Square drawn!")