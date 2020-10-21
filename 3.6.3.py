import requests
import pprint
list_numbers = []
params = {'json' : '', 'default' : 'Boring', 'blabla' : 'bebe'}

with open(r'D:\Programming\dataset_24476_3.txt') as inf, open(r'D:\Programming\fileout.txt', 'w', encoding='utf-8') as outf:
    for line in inf:
        list_numbers.append(line.rstrip())

numbers_request = list_numbers[0]
for i in range(1, len(list_numbers)):
    numbers_request += ','+list_numbers[i]
print(numbers_request)

outf = open(r'D:\Programming\fileout.txt', 'w', encoding='utf-8')
request = requests.get('{site}{number}/math'.format(site = 'http://numbersapi.com/', number = numbers_request), params=params).json()

for i in list_numbers:
    if request[i] == 'Boring':
        print(i, '-', 'Boring')
        try:
            pass
            outf.write('Boring\n')
        except Exception:
            pass
    else:
        print(i, '-', 'Interesting')
        try:
            pass
            outf.writelines('Interesting\n')
        except Exception:
            pass
#str = 'Interesting' if request['found'] else 'Boring'
#print(str, request['found'])
outf.close()
