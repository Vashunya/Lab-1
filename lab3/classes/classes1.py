class String:
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())
    

my_string = String()
my_string.getString()
my_string.printString()