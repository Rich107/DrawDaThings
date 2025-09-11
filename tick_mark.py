import pyautogui
import time
import math

pyautogui.PAUSE = 0

# Wait a few seconds to give you time to switch to the Slack window
time.sleep(0)

# Get the current mouse position
center_x, center_y = pyautogui.position()

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

# Draw the tick mark
tick_size = 40

# Draw the first part of the tick (shorter line going down-left to center)
pyautogui.moveTo(center_x - tick_size//2, center_y)
pyautogui.mouseDown()
pyautogui.moveTo(center_x - tick_size//4, center_y + tick_size//3)
pyautogui.mouseUp()

# Draw the second part of the tick (longer line going from center up-right)
pyautogui.moveTo(center_x - tick_size//4, center_y + tick_size//3)
pyautogui.mouseDown()
pyautogui.moveTo(center_x + tick_size//2, center_y - tick_size//2)
pyautogui.mouseUp()

print("Circle with tick mark drawn!")