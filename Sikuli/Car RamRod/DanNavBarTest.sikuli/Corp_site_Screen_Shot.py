#settings
Screen=Screen(1)#Change 1 to 0 if using only 1 monitor
#Variables
myApp = App("Firefox")
baseurl = "http://www.buddymedia.com" #This is the base URL
found = " image found"
notfound = " image not found"
products_menu = 0
solutions_menu = 0
services_menu = 0
clients_menu = 0 
resources_menu = 0

products_menu_total = 0
solutions_menu_total = 0
services_menu_total = 0
clients_menu_total = 0
resources_menu_total = 0
        
        
if not myApp.window(): # no window(0) - Firefox not open
        App.open("c:\\Program Files\\Mozilla Firefox\\Firefox.exe") # Windoze
        wait(2)
myApp.focus()
wait(1)
type("l", KEY_CMD) # switch to address field in firefox / chrome / safari. Need to add in conditional using F6 in IE
type(baseurl + "\n")

#this test assures that all the images in the product menu exist.
if Screen.exists("PRODUCTS-2.png"):
    Screen.click ("PRODUCTS-2.png")
    if Screen.exists("ALLPRODUCTS-6.png"):
        products_menu = products_menu + 1 
        products_menu_total = products_menu_total + 1
        print "All product" + found
    else:
            print "All product" + notfound
            products_menu_total = products_menu_total + 1
            exit
    if Screen.exists("CONVERSATION-1.png"):
        products_menu = products_menu + 1 
        products_menu_total = products_menu_total + 1
        print "ConversationBuddy" + found
    else:
            print "ConversationBuddy" + notfound
            products_menu_total = products_menu_total + 1        
            exit
    if Screen.exists("PROFILEBLJDD.png"):
        products_menu = products_menu + 1 
        products_menu_total = products_menu_total + 1
        print "ProfileBuddy" + found
    else:
            print "ProfileBuddy" + notfound
            products_menu_total = products_menu_total + 1        
            exit            
    if Screen.exists("CONVERSIONBU.png"):
        products_menu = products_menu + 1 
        products_menu_total = products_menu_total + 1
        print "ConversionBuddy" + found
    else:
            print "conversionBuddy" + notfound
            products_menu_total = products_menu_total + 1        
            exit  
    exit
    if Screen.exists("REACHBUDDY.png"):
        products_menu = products_menu + 1 
        products_menu_total = products_menu_total + 1
        print "ReachBuddy" + found
            
    else:
            print "reachBuddy" + notfound           
            products_menu_total = products_menu_total + 1         
            exit      
    if Screen.exists("ANALYTICS.png"):
        products_menu = products_menu + 1 
        products_menu_total = products_menu_total + 1        
        print "Analytics" + found
    else:
            print "Analytics" + notfound
            products_menu_total = products_menu_total + 1         
            exit
    if Screen.exists("DASHBOARD.png"):
        products_menu = products_menu + 1 
        products_menu_total = products_menu_total + 1
        print "Dashboard" + found
    else:
            print "Dashboard" + notfound
            products_menu_total = products_menu_total + 1                    
            exit 

else: 
    print "products menu" + notfound
#output what worked and what did not work
print products_menu, "out of ", products_menu_total, " works"

#this test assures that all the images in the solutions menu exist.

if Screen.exists("SOLUTIONS.png"):
    Screen.click ("SOLUTIONS.png")
    if Screen.exists("ALLSOLUTIONS.png"):
        solutions_menu = solutions_menu + 1 
        solutions_menu_total = solutions_menu_total + 1
        print "Solutions" + found
    else:
            print "Solutions" + notfound
            solutions_menu_total = solutions_menu_total + 1
            exit
    if Screen.exists("CHALLENGESSO.png"):
        solutions_menu = solutions_menu + 1 
        solutions_menu_total = solutions_menu_total + 1
        print "Challenges + solutions" + found
    else:
            print "challenges + solutions" + notfound
            solutions_menu_total = solutions_menu_total + 1        
            exit
    if Screen.exists("CASESTUDIES.png"):
        solutions_menu = solutions_menu + 1 
        solutions_menu_total = solutions_menu_total + 1
        print "Case studies" + found
    else:
            print "casestudies" + notfound
            solutions_menu_total = solutions_menu_total + 1        
            exit            

else: 
    print "solutions menu" + notfound

print solutions_menu, "out of ", solutions_menu_total, " works"

#this test assures that all the images in the services menu exist.
if Screen.exists("SERVICES.png"):
    Screen.click ("SERVICES.png")
    if Screen.exists("BUDDYMEDIAUN.png"):
        services_menu = services_menu + 1 
        services_menu_total = services_menu_total + 1
        print "Buddy Media University" + found
    else:
            print "Buddy Media University" + notfound
            services_menu_total = services_menu_total + 1
            exit
    if Screen.exists("SUPPORT.png"):
        services_menu = services_menu + 1 
        services_menu_total = services_menu_total + 1
        print "Support" + found
    else:
            print "Support" + notfound
            services_menu_total = services_menu_total + 1        
            exit
    if Screen.exists("DEVELOPMENTP.png"):
        services_menu = services_menu + 1 
        services_menu_total = services_menu_total + 1
        print "Development Platform" + found
    else:
            print "Development Platform" + notfound
            services_menu_total = services_menu_total + 1        
            exit            

else: 
    print "services menu" + notfound

print services_menu, "out of ", services_menu_total, " works"

#this test assures that all the images in the clients menu exist.

if Screen.exists("CLIENTS.png"):
    Screen.click ("CLIENTS.png")
    if Screen.exists("ALLCLIENTS.png"):
        clients_menu = clients_menu + 1 
        clients_menu_total = clients_menu_total + 1
        print "All Clients" + found
    else:
            print "All Clients" + notfound
            clients_menu_total = clients_menu_total + 1
            exit
    if Screen.exists("CLIENTSBYIND-2.png"):
        clients_menu = clients_menu + 1 
        clients_menu_total = clients_menu_total + 1
        print "Clients by industry" + found
    else:
            print "Clients by industry" + notfound
            clients_menu_total = clients_menu_total + 1        
            exit
else: 
    print "clients menu" + notfound

print clients_menu, "out of ", clients_menu_total, " works"

#this test assures that all the images in the resources menu exist.

if Screen.exists("RESOURCES.png"):
    Screen.click ("RESOURCES.png")
    if Screen.exists("ALLRESOURCES.png"):
        resources_menu = resources_menu + 1 
        resources_menu_total = resources_menu_total + 1
        print "All Resources" + found
    else:
            print "All Resources" + notfound
            resources_menu_total = resources_menu_total + 1
            exit
    if Screen.exists("WHITEPAPERS.png"):
        resources_menu = resources_menu + 1 
        resources_menu_total = resources_menu_total + 1
        print "White papers" + found
    else:
            print "White papers" + notfound
            resources_menu_total = resources_menu_total + 1        
            exit
    if Screen.exists("WEBINARS-1.png"):
        resources_menu = resources_menu + 1 
        resources_menu_total = resources_menu_total + 1
        print "Webinars" + found
    else:
            print "Webinars" + notfound
            resources_menu_total = resources_menu_total + 1        
            exit
    if Screen.exists("EVENTS-1.png"):
        resources_menu = resources_menu + 1 
        resources_menu_total = resources_menu_total + 1
        print "Events" + found
    else:
            print "Events" + notfound
            resources_menu_total = resources_menu_total + 1        
            exit            

else: 
    print "resources menu" + notfound

print resources_menu, "out of ", resources_menu_total, " works"
