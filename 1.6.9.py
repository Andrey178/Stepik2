import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, T):
        Loggable.log(self, T)
#        list.append(self, T)
        print('-----')
        self.log(T)
        super(LoggableList, self).log(T)
    def append2(self, T):
        self.append(T)



A = LoggableList()
A.append(5)
A.append2(6)
