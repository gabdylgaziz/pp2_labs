class String:
    def __init__(self, getString):
        self.getString = getString
    def printString(self):
        return self.getString.upper()
        
s = String('Hello, World!')
print(s.printString())
        
        