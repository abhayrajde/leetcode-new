class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.values = []
        self.a = 0
        self.b = -1
        self.totalA = 0
        self.totalB = 0

    def next(self, val: int) -> float:
        self.b += 1
        if self.b - self.a + 1 > self.size:
            self.totalA += self.values[self.a]
            self.a += 1
        self.values.append(val)
        self.totalB += val
        return (self.totalB - self.totalA) / (self.b - self.a + 1)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
