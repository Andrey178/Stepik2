s, a, b, changecount = ['abab', 'ab', 'ba', 0]
#s, a, b, changecount = [input() for i in range(3)] + [0]
while changecount <= 1000:
    if a in s:
        s = s.replace(a, b)
        changecount += 1
    else:
        break
print(changecount if changecount <= 1000 else 'Impossible')