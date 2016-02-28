array = [26, 44, 60, 74, 87, 86, 79, 24, 43, 68]
print "Array before it is sorted: " + str(array)

class shell():

    def sort(self, a):
        self.N = len(a)

        h_array = [1]
        while (h_array[-1] < self.N/3):
            h_array.append(3*h_array[-1] + 1)

        h_array.reverse()
        print h_array
        h = 1
        while (h>=1):
            try:
                h = h_array.pop()
            except:
                break
            for element in range(h-1, self.N, 1):
                for j in range(element, 0+h,-h):
                    if self.less(a[j], a[j-h]):
                        self.exch(a, j, j-h)

    def exch(self, ar, i, j):
        swap = ar[i]
        ar[i] = ar[j]
        ar[j] = swap

    def less(self, v, w):
        return v < w


sort = shell()
sort.sort(array)
print "Array after it is sorted: " + str(array)