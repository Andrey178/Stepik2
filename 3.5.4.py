import json

listgroups = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'
#listgroups = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
#listgroups = input()
class1 = json.loads(listgroups)
parentsamount = {}
parentssum = {}
#setparents = ()

for ind in class1:
    parentsamount[ind['name']] = ind['parents']
    parentssum[ind['name']] = set()
#print(parentssum)
#print(parentsamount)

def checkparent(class_name, parents):
#    print(class_name, len(class_name), end=' -- ')
    if len(parents) != 0:
        for _ in parents:
            parentssum[_].add(class_name)
#            print('(', _, parentssum[_], ')')
            checkparent(class_name, parentsamount[_])
#    print('\nend', parentssum)


for ind, item in parentsamount.items():
#    print('check', ind, '-', item)
    checkparent(ind, item)
#    setparents = set()
#    print(parentssum)

print()
#    print(ind['name'], ':', (int(len(ind['parents']))))
for ind, item in sorted(parentssum.items()):
#    print(ind, ':', len(item)+1)
    print('{n} : {c}'.format(n = ind, c = len(item)+1))
