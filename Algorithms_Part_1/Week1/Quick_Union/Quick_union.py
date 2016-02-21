class QuickUnion(object):
    def __init__(self, Length_of_array):
        self.length = Length_of_array
        self.Find_array= range(Length_of_array)
        pass

    def Connected(self, x,y):
        return self.__root(self.Find_array[x]) == self.__root(self.Find_array[y])

    def Union(self,index_a, index_b):
        i = self.__root(index_a)
        j = self.__root(index_b)
        self.Find_array[i] = j

    def __root(self, x):
        while(self.Find_array[x] != x):
            x = self.Find_array[x]
        return x