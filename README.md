CSGORoll Daily Collector
---------------
A bot to auto-collect dailies in the background, allowing for peace of mind

This comes with Auto-Login, Auto-Stashing, and Immediate Coin Balance Updates within the executable 

The script will simply open all cases > then stash the balance

There are options on if you want to stash or not and for how long (1hr ~ 7 days)

Simply turn off the stash lock feature when you want to withdraw

With that said, the setup instructions are below 


Important Downloads (Required)
--------------------------------------
1> Download Python from the official website

2> Open Command Prompt in Administrator Mode and enter the following:
```
	pip install schedule
	pip install -U selenium
	pip install webdriver-manager
```
This is to download scripting libraries

Important Setup Information (Required)
--------------------------------------
1> Download Google Chrome if you haven't already

2> Download VSCode or any code editor
	- Install the Python Addon to VSCode
 
3> Open the "Daily Collector" folder in VSCode (or your code editor)

4> Go to web\json\settings.json and open the file

  - There are a few fields to replace:
    
  - "profilePath": The path to your Google Chrome Profiles (details below)
    
	- "isStashed": Enter "Yes" to lock your coins on stash and "No" to not lock it
    
	- "stashOption": The duration of the lock
	("1" = 1hr | "2" = 2hrs | "3" = 4hrs | "4" = 8hrs | "5" = 12hrs | "6" = 1 day | "7" = 7 days)

	- "levelOption": The case level you have unlocked right now
	(LV2 = 1 | LV10 = 2 | LV20 = 3 | LV30 = 4 | LV40 = 5| LV50 = 6 | LV60 = 7 | LV70 = 8| LV80 = 9
	LV90 = 10| LV100 = 11)

Note: Only replace the contents inside the ""

Ex: "isStashed": "No"    ---Is Replaced to--->     "isStashed": "Yes"

Finding Profile:

1> Type "chrome://version/" into your Google Chrome

2> Find the Profile Path
	-Example : "C:\Users\YOUR_WINDOWS_USERNAME\AppData\Local\Google\Chrome\User Data\Default"
 
3> Once you put the Profile Path into "settings.json", you will find that there are red lines
   This is normal. You just need to make all "\" in the Profile Path turn into "\\", which will solve the error 


Important Step (First Login)
---------------------------
You must first login once into your account for the script to run

1> Go into VSCode and open the "CSGORoll Daily Collector" folder

2> Run the browserSetup.py with the run button on the top right corner of VSCode
	- It will open a blank Google Chrome window
	- Simply log into your CSGORoll account


Scheduling the Script
---------------------------
Note: Schedule the script after all daily cases are off cooldown

Follow this Guide on how to schedule "script.py" to run every day
https://www.jcchouinard.com/python-automation-using-task-scheduler/

The python file you want to schedule is "script.py"

Pictures are in the "Installation Guide" folder to help you understand what it should look like

After you schedule it, the script will run on login 
Once, your daily cases have reset, simply restart and it will auto-claim 
