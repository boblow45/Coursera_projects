import numpy as np
array = np.random.rand(20)
print "Array before it is sorted: " + str(array)

class Selection(object):

    def __init__(self):
        pass

    def sort(self, array):
        n = len(array)
        for element in range(n):
            minimum  = element
            for j in range(element, n, 1):
                if (self.less(array[j], array[minimum])):
                    minimum = j
            self.exch(array, element, minimum)

    def exch(self, array, i, j):
        swap = array[i]
        array[i] = array[j]
        array[j] = swap

    def less(self, v, w):
        return v < w

sort = Selection()
sort.sort(array)
print "Array after it is sorted: " + str(array)