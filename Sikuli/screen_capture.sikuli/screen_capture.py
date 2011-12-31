#Script gets full screen resolution, takes a screenshot and then moves it to the project folder with the filename 
#of "out.png"
import shutil
Screen = Screen(0)
file_loc  = capture(Screen.getBounds())
shutil.move(file_loc, getBundlePath() + "\\" + "out.jpg")
