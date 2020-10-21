class multifilter:
    def judge_half(pos, neg):
    # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return True if pos >= neg else False

    def judge_any(pos, neg):
    # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return True if pos > 0 else False

    def judge_all(pos, neg):
    # допускает элемент, если его допускают все функции (neg == 0)
        return True if neg==0 else False

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iter_ = iterable
        self.func_ = funcs
        self.judge = judge
 #   def __next__(self):
 #       self.iterindx += 1
#        if self.iterindx < len(self.iter_):
#           return self.iter_[self.iterindx]
#        else:
#            raise StopIteration
    def __iter__(self):
        for _ in self.iter_:
            result = []
            for i in self.func_:
                result.append(i(_))
            if self.judge(result.count(True), result.count(False)):
                yield _
#        return self
        # возвращает итератор по результирующей последовательности

def mul2(x):
       return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]
print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))