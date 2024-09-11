import pyautogui
import time
import math

pyautogui.PAUSE = 0

# Wait a few seconds to give you time to switch to the Slack window
time.sleep(0)

# Set the starting position for the smiley face (center of the face)
# center_x, center_y = 600, 400  # Adjust these values as needed

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

# Draw the left eye
eye_x_offset = 30
eye_y_offset = 30

pyautogui.moveTo(center_x - eye_x_offset, center_y - eye_y_offset)
pyautogui.mouseDown()
pyautogui.mouseUp()

# Draw the right eye
pyautogui.moveTo(center_x + eye_x_offset, center_y - eye_y_offset)
pyautogui.mouseDown()

pyautogui.mouseUp()

# Draw the smile
smile_radius = 60
smile_y_offset = 10

pyautogui.PAUSE = 0

pyautogui.moveTo(
    center_x + smile_radius * math.cos(math.radians(30)),
    center_y + smile_y_offset + smile_radius * math.sin(math.radians(30)),
)
pyautogui.mouseDown()

for i in range(30, 151, 2):
    angle = math.radians(i)
    x = center_x + smile_radius * math.cos(angle)
    y = center_y + smile_y_offset + smile_radius * math.sin(angle)
    pyautogui.moveTo(x, y)

pyautogui.mouseUp()

print("Smiley face drawn with continuous lines!")
