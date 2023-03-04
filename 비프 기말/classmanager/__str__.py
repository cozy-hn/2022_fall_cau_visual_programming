class Slist:
    def __init__(self):
        self.head=None
        self.size=0
    def add(self):
        self.size=self.size+ 1
    def __str__(self):
        return '%d' %self.size
s = Slist()
print(s)