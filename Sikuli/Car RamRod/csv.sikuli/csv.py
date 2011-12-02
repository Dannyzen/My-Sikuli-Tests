import csv
import StringIO
scsv = """1,2,3
a,b,c
d,e,f"""

#f = links.csv(scsv)
reader = csv.reader(f, delimiter=',')
for row in reader:
    print '\t'.join(row)