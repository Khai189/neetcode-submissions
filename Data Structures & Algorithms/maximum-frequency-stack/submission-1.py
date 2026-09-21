class FreqStack:

    def __init__(self):
        self.freqs = defaultdict(int)
        self.group = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freqs[val] + 1
        self.freqs[val] = f

        if f > self.max_freq:
            self.max_freq = f

        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freqs[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()