
classbase = {'object':[]}
lines = []

def checkroot(cls, inher):
    if (cls not in classbase and cls not in classbase['object'] or
            inher not in classbase and inher not in classbase[
        'object']):
        print('no such class, ', end='')
        return False
    if cls == inher:
        return True
    elif cls in classbase['object']:
        return False
    elif inher in classbase[cls]:
        return True
    else:
        for _ in classbase[cls]:
            if checkroot(_, inher):
                return True
        return False

def checkquest():
#    global lines
#    print(lines[0])
    for _ in range(1, int(lines[0])+1, 1):
        inher, clas = lines[_].split()
        print(inher, 'for', clas, end=' ')
        if checkroot(clas, inher):
            print('Yes')
        else:
             print('No')


def readclasses():
#    print(lines[0].strip())
    for i in range(1, int(lines[0])+1):
        print(i, ' ', lines[1], end='')
        str = lines[1].strip()
        lines.pop(1)
        if str.isalnum():
            classbase['object'].extend([str])
        else:
            clas, roots = str.split(' : ')
            inher = roots.split()
            classbase.setdefault(clas, [])
            classbase[clas].extend(inher)
    lines.pop(0)
#    lines = lines[int(lines[0]) + 1:]
    print(classbase)


def readinput():
    with open ("d:\programming\\filein.txt") as inf:
        lines.extend(inf.readlines())
#    print(*lines)

readinput()
readclasses()
checkquest()


