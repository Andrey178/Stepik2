#from itertools import takewhile
def primes(limit=110):
    x = 2
    yield x
    #while True:
    while x < limit:
        x += 1
        isp = True
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                isp = False
                break
        if isp:
            yield x

#print((lambda x: x <= 31) (primes()))
#print(list(map(lambda x : x * 2 , primes())))
for _ in primes(10):
    print(_)
for _ in primes():
    print(_)
print(*primes(31))
yo = primes()
for i in range(5):
    print(next(yo))