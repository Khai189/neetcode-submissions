class FreqStack:

    def __init__(self):
        
        self.mp = defaultdict(int)

        self.max_freq = 0
        self.stack = {}

    def push(self, val: int) -> None:
        self.mp[val]+=1
        if self.mp[val] > self.max_freq:
            self.max_freq = self.mp[val]
            self.stack[self.mp[val]] = []
        
        self.stack[self.mp[val]].append(val)
        


    def pop(self) -> int:
        res = self.stack[self.max_freq].pop()
        self.mp[res]-=1
        if self.stack[self.max_freq] == []:
            self.max_freq-=1
        
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()