class pushdown_stack:
    def __init__(self):
        self.vals = []
        self.nexts = []
    def put(self, value):
        self.vals = [value] + self.vals
        if self.nexts:
            self.nexts = self.vals[1] + self.nexts
        else:
            self.nexts = [None]
    def get(self):
        self.vals = self.vals[1:]
        self.nexts = self.nexts[1:]
