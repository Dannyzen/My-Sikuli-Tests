another_num = int(1) 
num = int(0) #getting the starting number .
Screen=Screen(1)#Change 1 to 0 if using only 1 monitor
name=input("What is your .dev username? EG: erica")

results = []
my_file = file("/users/dannyrosen/Desktop/test.txt", "r")
for line in my_file:
      results.append(line.replace("\n", " "))
x = (len(results))


def list():
        
    results = []
    my_file = file("/users/dannyrosen/Desktop/test.txt", "r")
    for line in my_file:
      results.append(line.replace("\n", " "))

    for i in range (len(results)):
        address=(results[num])
        global address    
def count():
    global another_num
    global num
    #if (num < i): #start the loop .
    num = num + another_num #add the value to [num]
    #    print num
    #else:
    #    print num

def fc():
    run
    list()
    openApp("Firefox")
    wait(3)
    type("l", KEY_CMD) # switch to address field
    wait (1)
    paste(address)
    type(Key.ENTER)
    

while (num < x):
    run
    fc()

run
fm()