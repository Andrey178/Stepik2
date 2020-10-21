s, t, count = ['abababa', 'aba', 0]
#s, t, count = [input() for _ in range(2)] + [0]
while t in s:
    s = s[s.find(t) + 1:]
    print(s)
    count += 1
print(count)