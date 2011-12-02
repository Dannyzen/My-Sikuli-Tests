openApp("terminal")
wait("1319056852637.png")
type("mkdir ~/Desktop/testresults") #make parent directory
type(Key.ENTER)
type("Date | pbcopy") #copy time stamp
type(Key.ENTER)
type("mkdir ~/Desktop/testresults/'")
keyDown(Key.CMD)
type("v") #make timestamped child directory
keyUp(Key.CMD)
type("'")
type(Key.ENTER)
type("mv ~/Desktop/Screen* ~/Desktop/testresults/'")
keyDown(Key.CMD)
type("v")
keyUp(Key.CMD)
type("'")
type(Key.ENTER) #move files
closeApp("terminal")