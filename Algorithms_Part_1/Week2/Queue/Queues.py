class Stack(object):
    def __init__(self):
        self.s = [None]
        self.tail = 0
        self.head = 0
        self.length = 1
        pass

    def enqueue(self, item):
        if (self.tail == self.length):
            # the following line of code will allow the array to remain as a power of 2. The code finds the length of array
            # required to to fit the old data to the nearest power of two and doubles it
            if (self.tail % self.head):
                self.length = (self.tail - self.head + 1) * 2
            else:
                self.length = (self.tail - self.head) * 2

            self.__resize(self.length)
        self.tail += 1
        self.s[self.tail] = item
        pass

    def dequeue(self):

        dummy = self.s[self.head]
        self.s[self.head] = None
        self.head += 1

        data_in_array = self.tail - self.head

        if (self.tail >0 and data_in_array == self.length/4):
            self.length = self.length/2
            self.__resize(self.length)
        return dummy

    def isEmpty(self):
        return (self.tail - self.head) == 0

    def size(self):
        return (self.tail - self.head + 1)

    def __resize(self, capacity):
        self.length = capacity
        copy = [None]*capacity
        for element in range(self.tail - self.head):
            copy[self.head + element] = self.s[self.head + element]
        self.s = copy

        self.tail -= self.head
        self.head = 0

