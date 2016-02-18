class QuickFind(object):
    def __init__(self, Length_of_array):
        self.length = Length_of_array
        self.Find_array= range(Length_of_array)
        pass

    def Connected(self, x,y):
        return self.Find_array[x] == self.Find_array[y]

    def Union(self,index_a, index_b):
        p = self.Find_array[index_a]
        q = self.Find_array[index_b]

        if p == q:
            return
        else:
            for element in range(self.length):
                if self.Find_array[element] == p:
                    self.Find_array[element] = q
            return

point_a = [2,3,3,7,9,0]
point_b = [5,8,1,6,4,4]

quickfind = QuickFind(10)
for element in range(len(point_a)):
    quickfind.Union(point_a[element], point_b[element])

print str(quickfind.Find_array)