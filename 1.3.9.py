
def closest_mod_5(x):
    for i in range(x, x+5):
        if i%5 == 0:
            return i

def closest_mod2_5(x):
    while x%5 != 0:
        x += 1
    return x
x = 7
print(closest_mod2_5(x))