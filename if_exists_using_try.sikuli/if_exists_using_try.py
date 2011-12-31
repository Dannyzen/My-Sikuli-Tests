#pulls up task manager, then uses try to conifrm if a item exists.
def google_works():
    keyDown(Key.CTRL + Key.SHIFT + Key.ESC)
    keyUp()
    type(Key.ALT + "f" + "n")
    wait(2)
    type ("firefox")
    type (Key.ENTER) 
    wait(2)
    try: 
        find("le-3.png")
        print ("it's fucking there")
        #a bit of a terse output, heh.
    except:
        print ("shit's not there")