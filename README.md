# DrawDaThings

## Why:
When using screen sharing tools like Zoom and Slack they allow you to write on the screen. Primarily this is used to highlight areas of interest but it can also be fun to draw to communicate without interrupting people who are currently talking.

## Install:
`pyautogui` needs to be installed on the python interpreter that you are going to be running it from. 

``` bash
python3 -m pip install pyautogui
```

If running from Alfred, it has access to your host python. So if you are running it using Alfred you will need to install it on your host python.  

Screen shot for workflows menu

> [!NOTE]
> If you want to run this from Alfred using a workflow you will need the paid for power pack.



## How:
If you want to make your own drawings feel free to create a PR and add it here. 

The current drawings were first drafted using ChatGPT. Initially the drawings did not work well and had timing issues. Thus I have created a troubleshooting section below in case anyone would like to try their hand at making some new ones. Please also feel free to submit PRs for overcoming issues in the trouble shooting steps below.


## Troubleshooting:

### Mouse is jumping
This might be because you are not giving the cursor enough time to register its click in between actions. 
When making the smily faces I found that it would stay clicked down or miss things out if this was set to 0 all the time.
Try giving it a little more time by changing the below setting:

``` python
pyautogui.PAUSE = 0.1
```

### Mouse is moving really slowly
-  Reduce the number of points being generated. 
-  Change the gap between actions to zero or a very low number.

``` python
pyautogui.PAUSE = 0.1
```

> [!Tip]
> Try changing this setting at different stages of the drawing to see what makes the most consistent outcome. 
