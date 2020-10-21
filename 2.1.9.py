class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
#            super(PositiveList, self).append(x)
            super().append(x)
        else:
            raise NonPositiveError

list = PositiveList()
list.append(4)
#list.append(-1)

