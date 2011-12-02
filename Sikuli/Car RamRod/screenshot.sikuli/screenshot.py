banana = input("What do you want to look at pictures of?")
openApp("FireFox")
find("1319135989759.png")
type("l", KEY_CMD) # switch to address field
type("google.com/imghp?hl=en&tab=wi")
type(Key.ENTER)
wait(2)
paste(banana)
wait(1)
type(Key.ENTER)
wait(1)
keyDown(Key.SHIFT+Key.CMD)
type("4")
wait(1)
keyUp(Key.SHIFT+Key.CMD)
wait(1)
type(Key.SPACE)
click("leG0.png")
wait(2)
openApp("Finder")
find("AllMyFilesAi.png")

if exists(Pattern("Desktop.png").similar(0.89)):
     click("Desktop.png")
else:
    click("Qneskmv.png")
    
if exists(Pattern("1319136642723.png").similar(0.97)):
    click("1319136642723.png")
click("DateModified.png")
wait(1)
type(Key.DOWN)
wait(1)
if exists("IScreenShot.png"):
    type(Key.SPACE)
else:
     click("1319135850430.png")
     click("DateModified.png")
     wait(2)
     type(Key.DOWN)
     type(Key.SPACE)
popup("Enjoy your pictures!")