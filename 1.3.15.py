list = [10, 5]
n, k = list


def C(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        r = C(n - 1, k) + C(n - 1, k - 1)
    return r


print(C(n, k))
