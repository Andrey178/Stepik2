class MoneyBox:
    capacity = 10

    def __init__(self, capacity=0):
        self.capacity = capacity

    def can_add(self, v):
        if self.capacity - v >= 0:
            return True
        else:
            return False

    def add(self, v):
        self.capacity -= v

mb = MoneyBox(100)
print(mb.can_add(20))
print(mb.capacity)
print(MoneyBox.capacity)
mb.add(20)
