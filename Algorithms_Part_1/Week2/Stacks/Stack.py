class Stack(object):
    def __init__(self):
        self.s = [None]
        self.N = 0
        self.length = 1
        pass

    def push(self, item):
        if (self.N == self.length):
            self.__resize(2*self.length)
        self.N += 1
        self.s[self.N] = item
        pass

    def pop(self):
        self.N -= 1
        dummy = self.s[self.N]
        self.s[self.N] = "Null"
        if (self.N >0 and self.N == self.length/4):
            self.__resize(self.length/2)
        return dummy

    def isEmpty(self):
        return  self.N == 0

    def size(self):
        return (self.N + 1)

    def __resize(self, capacity):
        self.length = capacity
        copy = [None]*capacity
        for element in range(self.N):
            copy[element] = self.s[element]
        self.s = copy


#######################################
##               Client              ##
#######################################

File_name = "input6"
results = []
with open(File_name + '.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(' '))

stack = Stack()
for element in range(len(results)):
    if (results[element] == "-"):
        print(stack.pop())
    else:
        stack.push(results[element])