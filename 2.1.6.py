try:
    print(ZeroDivisionError.mro())
    print(AssertionError.mro())
    print(ArithmeticError.mro())
    y = 5 + 'a'
    x = 5 / 0

except (ArithmeticError, AssertionError, ZeroDivisionError) as e:
    if isinstance(e, ZeroDivisionError):
        print('ZeroDivisionError')
    if isinstance(e, ArithmeticError):
        print('ArithmeticError')
    if isinstance(e, AssertionError):
        print('AssertionError')
    print(e)