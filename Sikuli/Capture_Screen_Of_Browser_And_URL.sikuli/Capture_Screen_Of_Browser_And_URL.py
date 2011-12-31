#This script is a function called "site_shooter()" which takes 3 variables: Browser [required], url [required]
#and full[defaulted to 0, not required]. It launches a browser, pushes the url into it and takes a screenshot of
#that page. If full is set to 1 it will maximize the browser window.

import os
import shutil
Screen = Screen(0)


def shoot():    
    file_loc  = capture(Screen.getBounds())
    shutil.move(file_loc, getBundlePath() + "\\" + "out.jpg")
    
def site_shooter(browser,url,full=0):  
# Figure out what os we're in 
    myOS = Env.getOS()
    if myOS == OS.MAC:
        App.open(browser)
        #Gotta expand this out to work with macs.
    else:
        #we're in windows' world...
        keyDown(Key.CTRL + Key.SHIFT + Key.ESC)
        App.focus("taskmgr.exe")
        keyUp()
        type(Key.ALT + "f" + "n")
        wait(2)
        paste (browser)
        type (Key.ENTER)
        App.focus("taskmgr.exe")
        type(Key.ALT + "f" + "x")
        #new_b = (browser + ".exe") #debugging a bit
        #App.focus(new_b)
    wait(2) 
    keyDown(Key.ALT + "D")
    keyUp()
    paste (url)
    type (Key.ENTER)
    wait(10)
    if browser != "iexplore":
        if full == 1:
            type(Key.F11)
            wait(2)
            shoot() 
    else:
        if full == 1:
            keyDown(Key.ALT + Key.ENTER)
            keyUp()
            wait(2)
            shoot() 
    
    exit(1)

site_shooter("chrome","aol.com",1)