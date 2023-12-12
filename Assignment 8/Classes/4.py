class PairSum:
    def __init__(self, numbers, target):
        self.numbers = numbers
        self.target = target
    def find_pair(self):
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == self.target:
                    return i, j
        return None