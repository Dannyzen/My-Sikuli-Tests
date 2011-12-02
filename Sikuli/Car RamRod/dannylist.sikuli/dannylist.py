def list():
    name=input("What is your .dev username? EG: erica")
 
    results = []
    my_file = file("/users/patrick.foley/Desktop/test.txt", "r")
    for line in my_file:
      results.append(line.replace("\n", " "))

    for x in range (len(results)):
        address=(results[4])
    print (len(rsults)))    

run
list()