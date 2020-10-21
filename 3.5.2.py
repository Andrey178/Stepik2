import csv
import time

start1 = time.time()
print(start1)
with open ("D:\Programming\Crimes.csv") as inf:
    reader = csv.DictReader(inf)
    crimecount = {'0': 0}
    for str in reader:
#        str = next(reader)
#        date = (str.get('Date').split()[0]).split('/')[2]
        date = str.get('Date')[6:10]
        crimename = str.get('Primary Type')
#        if date == '2015':
        if str.get('Date').find('2015'):
            crimecount[crimename] = crimecount.setdefault(crimename, 0) + 1
#            print(date, str.get('Date'), '-', crimename, '-', crimecount.get(crimename))
#    print(str)
maxcrime = max(crimecount.values())
for ind, item in crimecount.items():
    if item == maxcrime:
        print(ind)
        break
time.sleep(0.3)
print((time.time() - start1))