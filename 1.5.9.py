class Buffer:
    lst = list()
    def __init__(self):
        self.lst = list()
    def  add(self, *a):
        self.lst += a
        while len(self.lst) >= 5:
            print(sum(self.lst[0:5]))
            self.lst = self.lst[5:]
    def get_current_part(self):
        return self.lst
    def get_current_part2(self):
        self.lst = []
        return self.lst

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()

