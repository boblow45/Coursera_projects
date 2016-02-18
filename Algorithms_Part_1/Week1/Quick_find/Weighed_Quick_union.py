class QuickUnion(object):
    def __init__(self, Length_of_array):
        self.length = Length_of_array
        self.sz = [1]*Length_of_array
        self.Find_array= range(Length_of_array)
        pass

    def Connected(self, x,y):
        return self.__root(self.Find_array[x]) == self.__root(self.Find_array[y])

    def Union(self,index_a, index_b):
        i = self.__root(index_a)
        j = self.__root(index_b)
        if (i == j):
            return
        elif(self.sz[i] < self.sz[j]):
            self.Find_array[i] = j
            self.sz[j] += self.sz[i]

            return
        else:
            self.Find_array[j] = i
            self.sz[i] += self.sz[j]
            return

    def __root(self, x):
        while(self.Find_array[x] != x):
            #self.Find_array[x] = self.Find_array[self.Find_array[x]]
            x = self.Find_array[x]
        return x

#[5, 5, 1, 5, 1, 5, 1, 5, 5, 5]

point_a = [1, 5, 8, 5, 4, 1, 8, 7, 0]
point_b = [2, 0, 7, 9, 6, 6, 0, 3, 6]

quickfind = QuickUnion(10)
for element in range(len(point_a)):
    quickfind.Union(point_a[element], point_b[element])

print str(quickfind.Find_array)