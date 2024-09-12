# DrawDaThings

## Why:
When using screen sharing tools like Zoom and Slack they allow you to write on the screen. Primarily this is used to highlight areas of interest but it can also be fun to draw to communicate without interrupting people who are currently talking.

Example smiley in Miro:
<p align="center">
    <img width="485" alt="image" src="https://github.com/user-attachments/assets/484d84a4-e604-4fb3-8f33-22a122c8bc07">
</p>

## Install:
`pyautogui` needs to be installed on the python interpreter that you are going to be running it from. 

``` bash
python3 -m pip install pyautogui
```

If running from Alfred, it has access to your host python. So if you are running it using Alfred you will need to install it on your host python.  

Go to workflows, create new workflow. Pull in a 'hot key' trigger and 'run script' command and link them together:
<p align="center">
    <img width="925" alt="image" src="https://github.com/user-attachments/assets/76e3e947-8fee-4804-9188-9afc3bdb6b32">
</p>

Click on the hot key and press the set of keys you want to run your script:
<p align="center">
    <img width="537" alt="image" src="https://github.com/user-attachments/assets/3c8b178d-2155-44af-8541-4fd5ea9ba81d">
</p>


Paste in the code into the outcome run script action:
<p align="center">
    <img width="808" alt="image" src="https://github.com/user-attachments/assets/ec61c26e-5506-44f2-9d88-e8afa72f7768">
</p>

> [!NOTE]
> If you want to run this from Alfred using a workflow you will need the paid for power pack.

> [!WARNING]
> Once you start one of theses scripts it will keep running until you pull your mouse to the corner of the screen. This is an auto hot key setting that is configurable. Keep this in mind if you want to get ambitious with the size of your drawings.

## Using with Raycast

1. Find a place where to install `pyautogui`, then create a virtual env for it:

   ```
   # Example path
   cd /Users/john/.local/venvs
   python3 -m venv drawdatthings
   source drawdatthings/bin/activate
   pip install pyautogui
   ```
   
2. In Raycast, choose the "Create Script Command":
   ![create-script-command](https://github.com/user-attachments/assets/46eae271-118f-453f-8e60-2d7bb81469a1)

3. Fill in the form:
   a. Choose "Python" as template and "compact" as mode.
   b. Fill in a title and description as you prefer, that's how the script will appear in Raycast.
   c. The other fields don't matter much
   ![create-script-form](https://github.com/user-attachments/assets/8dc9a743-3c36-4c16-bfcb-5527232e36f5)

5. Press <kbd>⌘</kbd> + <kbd>Enter</kbd> to create the script, this will open a finder window to place the script on your filesystem. I recommend placing it in the folder you created earlier, `/Users/john/.local/venvs/drawdatthings` if we follow the example earlier.
6. Open the file with you favourite code editor, and change the code to the following:

   ```diff
   - #!/usr/bin/env python3
   + #!/Users/john/.local/venvs/drawdatthings/bin/python
    
     # Required parameters:
     # @raycast.schemaVersion 1
     # @raycast.title Draw smiling face
     # @raycast.mode compact
     
     # Optional parameters:
     # @raycast.icon 🤖
     
     # Documentation:
     # @raycast.author John Doe
   
   - print("Hello World!")
   + import pyautogui
   + ...
   ```
   
So, basically:

- Replace the shebang `#!/usr/bin/env python3` with the path to the Python that has `pyautogui` installed
- Replace `print("Hello World!")` by the script you want to run

Now test it by searching for the script title in Raycast:

![raycast-run-script](https://github.com/user-attachments/assets/bf3bec2f-067b-4aeb-93cb-066885ee094d)

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
pyautogui.PAUSE = 0
```

> [!Tip]
> Try changing this setting at different stages of the drawing to see what makes the most consistent outcome. 
