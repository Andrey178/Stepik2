def create(space, spacename):
    print('func create', space.upper(), 'in', spacename.upper())
    namespaces[space] = {'parent' : spacename, 'variables' : set()}
    variables[space] = []
    print(namespaces)
    print(variables)
def add(space, var):
    print('func add', var.upper(), 'in ', space.upper())
    variables[space] += [var]
    namespaces.get(space).get('variables').add(var)
    print(variables[space])
    print(namespaces.get(space).get('variables'))
def get(space, var):
#    print('func get', var.upper(), 'in', space.upper())
#    if var in variables.get(space):
    if var in namespaces.get(space).get('variables'):
        return space+'!'
    else:
 #       print('    go UP')
        if space == 'global' and var not in variables.get(space):
            return None
        return get(namespaces.get(space).get('parent'), var)


comndList = []
namespaces = {'global':  {'parent':  None,  'variables' :  set()}}
variables = {'global':[]}

with open("d:\programming\\filein.txt") as inf:
    for i in range(int(inf.readline())):
        comndList.append(inf.readline().split())

#print(*comndList)

for i in comndList:
    if i[0] == 'create':
        create(i[1], i[2])
    elif i[0] == 'add':
        add(i[1], i[2])
    elif i[0] == 'get':
        print(get(i[1], i[2]))

#print(namespaces)
#print(variables)


