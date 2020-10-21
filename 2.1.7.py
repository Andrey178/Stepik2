def inputInfo():
    classesDict = {}
    queryList = []
    for i in range(int(input().strip())):
        str = input().strip()
        if str.isalnum():
            classesDict[str] = []
        else:
            name, args = str.strip().split(' : ')
            classesDict[name] = set(args.strip().split())

    for i in range(int(input().strip())):
        queryList.append(input().strip())

    return classesDict, queryList


classesDict, queryList = inputInfo()
print(classesDict, queryList, sep='\n')
toRemoveList = []
appliedPar = set()

def checkPar(i):
    addToRemove = False
    if i in classesDict.keys() and len(classesDict[i]) > 0:
        for ii in classesDict[i]:
            if ii in appliedPar:
                addToRemove = True
                break
            else:
                addToRemove = checkPar(ii)
#    print('checkPar', addToRemove, toRemoveList)
    return addToRemove


def findPar(queryList):
    for i in queryList:
        if i in appliedPar:
            toRemoveList.append(i)
            continue
        else:
            appliedPar.add(i)
        if checkPar(i):
            toRemoveList.append(i)

findPar(queryList)
#print(classesDict.values())
for i in toRemoveList:
    print(i)
