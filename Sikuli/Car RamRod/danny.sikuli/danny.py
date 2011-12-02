Screen=Screen(1)#Change 1 to 0 if using only 1 monitor
name=input("What is your .dev username? EG: erica")

results = []
my_file = file("/users/patrick.foley/Desktop/test.txt", "r")
for line in my_file:
  results.append(line.replace("\n", " "))

for i in range (len(results)):
    address=(results[num])

print address

