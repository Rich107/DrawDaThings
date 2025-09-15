import pyautogui
import time
import math

pyautogui.PAUSE = 0

# Wait a few seconds to give you time to switch to the Slack window
time.sleep(0)

# Get the current mouse position
center_x, center_y = pyautogui.position()

# Draw the X mark
x_size = 80

# Draw the first diagonal line of the X (top-left to bottom-right)
pyautogui.moveTo(center_x - x_size//2, center_y - x_size//2)
pyautogui.mouseDown()
pyautogui.moveTo(center_x + x_size//2, center_y + x_size//2)
pyautogui.mouseUp()

# Draw the second diagonal line of the X (top-right to bottom-left)
pyautogui.moveTo(center_x + x_size//2, center_y - x_size//2)
pyautogui.mouseDown()
pyautogui.moveTo(center_x - x_size//2, center_y + x_size//2)
pyautogui.mouseUp()

# Draw the face circle
radius = 100
pyautogui.moveTo(
    center_x + radius, center_y
)  # Move to the starting point of the circle
pyautogui.mouseDown()

for i in range(0, 361, 2):
    angle = math.radians(i)
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    pyautogui.moveTo(x, y)

pyautogui.PAUSE = 0.1
pyautogui.mouseUp()