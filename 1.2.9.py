#objects = [i for i in range(5)]
#objects += [i for i in range(5)]
objects = [1, 2, 1, 2, 3]

ans = 0
objects2 =[]
for obj in objects: # доступная переменная objects
    if obj not in objects2:
        objects2.append(obj)
        print(obj)

print(len(objects2))
