
class ESAb:
    def __init__(self, T):
        self.T = T
        self.SAME = 'S'
        self.DIFF = 'D'
        self.arr = ['_' for _ in range(T)]
        self.assistarr = ['_' for _ in range(T)]
        self.i = 1
        self.same = -1
        self.diff = -1
        self.run()

    def change(self, vtype):
        for i in range(self.T):
            if self.assistarr[i] == vtype:
                self.arr[i] = '1' if self.arr[i] == '0' else '0'
    
    def read(self, n):
        init = self.i
        for i in range(init, init + int(n/2)):
            x = i-1
            y = self.T-i
            print(i, flush=True)
            self.arr[x] = input()
            print(y+1, flush=True)
            self.arr[y] = input()
            if self.arr[x] == self.arr[y]:
                if self.same < 0:
                    self.same = x
                self.assistarr[x] = self.assistarr[y] = self.SAME
            else:
                if self.diff < 0:
                    self.diff = x
                self.assistarr[x] = self.assistarr[y] = self.DIFF
            self.i += 1

        if self.i > int(self.T/2):
            return

        print(1 + self.same if self.same >= 0 else 1, flush=True)
        t1 = input()
        if self.same >= 0 and self.arr[self.same] != t1:
            self.change(self.SAME)

        print(1 + self.diff if self.diff >= 0 else 1, flush=True)
        t2 = input()
        if self.diff >= 0 and self.arr[self.diff] != t2:
            self.change(self.DIFF)
    
    def run(self):
        rounds = int((self.T-10) / 8)
        self.read(10)
        for r in range(rounds):
            self.read(8)
        last = self.T - (rounds * 8 + 10)
        if last > 0:
            self.read(last)


B, T = [int(v) for v in input().split()]
for case in range(B):
    arr = ESAb(T)
    print(''.join([x for x in arr.arr]), flush=True)
    if input() == 'N': 
        exit(1)


# python interactive_runner.py python local_testing_tool_04.py 0 -- python 04.py
