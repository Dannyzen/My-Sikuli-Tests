#settings
Screen=Screen(1)#Change 1 to 0 if using only 1 monitor
openApp("Firefox")
keyDown(Key.SHIFT+Key.CMD)
type("f")
keyUp(Key.SHIFT+Key.CMD)
type(Key.PAGE_UP)
type(Key.PAGE_UP)
type(Key.PAGE_UP)
type(Key.PAGE_UP)
keyDown(Key.SHIFT+Key.CMD)
type("4")
wait(1)
keyUp(Key.SHIFT+Key.CMD)
wait(1)
type(Key.SPACE)
Screen.click("BUDDYEEMEDIA.png")
type(Key.PAGE_DOWN)
keyDown(Key.SHIFT+Key.CMD)
type("4")
wait(1)
keyUp(Key.SHIFT+Key.CMD)
wait(1)
type(Key.SPACE)
click
if Screen.exists("1319471560747.png"):
    keyDown(Key.SHIFT+Key.CMD)
    type("4")
    wait(1)
    keyUp(Key.SHIFT+Key.CMD)
    wait(1)
    type(Key.SPACE)
    Screen.click("1319472217716.png")
else:
    keyDown(Key.SHIFT+Key.CMD)
    type("4")
    wait(1)
    keyUp(Key.SHIFT+Key.CMD)
    wait(1)
    type(Key.SPACE)
    Screen.click("1319472217716.png")
    type(Key.PAGE_DOWN)
    keyDown(Key.SHIFT+Key.CMD)
    type("4")
    wait(1)
    keyUp(Key.SHIFT+Key.CMD)
    wait(1)
    type(Key.SPACE)
    Screen.click("1319472217716.png")

keyDown(Key.SHIFT+Key.CMD)
type("f")
keyUp(Key.SHIFT+Key.CMD)
