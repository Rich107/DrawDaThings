# DrawDaThings

## Why:
When using screen sharing tools like Zoom and Slack they allow you to write on the screen. Primarily this is used to highlight areas of interest but it can also be fun to draw to communicate without interrupting people who are currently talking.

Example smiley in Miro:

<img width="485" alt="image" src="https://github.com/user-attachments/assets/484d84a4-e604-4fb3-8f33-22a122c8bc07">


## Install:
`pyautogui` needs to be installed on the python interpreter that you are going to be running it from. 

``` bash
python3 -m pip install pyautogui
```

If running from Alfred, it has access to your host python. So if you are running it using Alfred you will need to install it on your host python.  

Go to workflows, create new workflow. Pull in a 'hot key' trigger and 'run script' command and link them together:
<p align="center"><img width="925" alt="image" src="https://github.com/user-attachments/assets/76e3e947-8fee-4804-9188-9afc3bdb6b32"></p>

Click on the hot key and press the set of keys you want to run your script:
<img width="537" alt="image" src="https://github.com/user-attachments/assets/3c8b178d-2155-44af-8541-4fd5ea9ba81d">

Paste in the code into the outcome run script action:
<img width="808" alt="image" src="https://github.com/user-attachments/assets/ec61c26e-5506-44f2-9d88-e8afa72f7768">


> [!NOTE]
> If you want to run this from Alfred using a workflow you will need the paid for power pack.

> [!WARNING]
> Once you start one of theses scripts it will keep running until you pull your mouse to the corner of the screen. This is an auto hot key setting that is configurable. Keep this in mind if you want to get ambitious with the size of your drawings. 

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
