class ExtendedStack(list):

#    def append(self, T):
#        self.append(T)

#    def pop(self):
#        self.pop()

    def sum(self):
        # операция сложения
        self.append(self.pop() + self.pop())
#        print(self)
    def sub(self):
        # операция вычитания
        self.append(self.pop()-self.pop())
#        print(self)
    def mul(self):
        # операция умножения
        if len(self) > 1:
            self.append(self.pop() * self.pop())
#            print(self)
    def div(self):
        # операция целочисленного деления
        if len(self) > 1 and self[-2] != 0:
            self.append(self.pop()//self.pop())
#            print(self)

A = ExtendedStack()
for i in range(6):
    A.append(i)
    if i == 3:
        A.append(0)
print(A)
print('run')
#print(A.mainlist[-2])
A.sum()
A.sub()
A.mul()
A.div()
print(A)

