import numpy as np
#array = np.random.rand(20)
array = [26, 44, 60, 74, 87, 86, 79, 24, 43, 68]
print "Array before it is sorted: " + str(array)

class Selection(object):

    def __init__(self):
        self.count = 0
        pass

    def sort(self, array):
        n = len(array)
        for element in range(n):
            for j in range(element, 0, -1):
                if (self.less(array[j], array[j-1])):
                    self.exch(array, j, j-1)
                    self.count +=1
                    if self.count == 6: print array
                else: break

    def exch(self, array, i, j):
        swap = array[i]
        array[i] = array[j]
        array[j] = swap

    def less(self, v, w):
        return v < w

sort = Selection()
sort.sort(array)
print "Array after it is sorted: " + str(array)