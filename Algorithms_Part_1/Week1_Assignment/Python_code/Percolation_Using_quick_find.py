results = []
with open('input6.txt') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(' '))

results_int = []
for element in range(len(results)):
    #print ("On %d line of the text file" %element)
    new = []
    for i in range(len(results[element])):
        #print ("On %d value of the row %d of the file" %(i, element))
        dummy = results[element][i]
        if (dummy != "" and dummy !="," and dummy != " "):
            new.append(int(dummy))
        #else:
        #   new.append("")
    results_int.append(new)

class Percolation(object):
    def __init__(self, size):
        self.__rows = size + 2
        self.__columns = size
        self.new_cell_value = size*size + 2
        counter = 0
        self.__grid = []
        for row in range(self.__rows):
            dummy_row = []
            for column in range(self.__columns):
                if (row != 0 and counter == 0):
                    counter += 1

                dummy_row.append(counter)
                if (row != 0 and row != size+1):
                    counter += 1
                    continue
            self.__grid.append(dummy_row)
        #print str(self.__grid) + "\n"

    def Open(self, row, column):
        if self.isFull(row, column):
            if (column == 0):
                if (self.isOpen(row-1, column) or self.isOpen(row+1, column) or self.isOpen(row, column+1)):
                    self.__grid[row][column] = self.new_cell_value
                    #check the cell above to see if it is open
                    self.__cellCheck(row, column, row - 1, column)
                    #check the cell on the right of this cell to see if it is open
                    self.__cellCheck(row, column, row, column + 1)
                    # The following line of code is used to check if the cell below the opened cell is less than the value
                    # in the opened cell (Note, this is only done if the cell below is open). The grids values are changed in
                    # accordance if the cell is open
                    self.__cellCheck(row, column, row+1, column)
                else:
                    self.__grid[row][column] = self.new_cell_value
                    self.new_cell_value += 1
                #print "Need to add a section of code here for the checks"

            elif (column == self.__columns - 1):
                if (self.isOpen(row-1, column) or self.isOpen(row+1, column) or self.isOpen(row, column-1)):
                    self.__grid[row][column] = self.new_cell_value
                    self.__cellCheck(row, column, row-1, column)
                    self.__cellCheck(row, column, row+1, column)
                    self.__cellCheck(row, column, row, column-1)
                else:
                    self.__grid[row][column] = self.new_cell_value
                    self.new_cell_value += 1

            else:
                if (self.isOpen(row-1, column) or self.isOpen(row+1, column) or self.isOpen(row, column-1) or self.isOpen(row, column+1)):
                    self.__grid[row][column] = self.new_cell_value
                    self.__cellCheck(row, column, row-1, column)
                    self.__cellCheck(row, column, row+1, column)
                    self.__cellCheck(row, column, row, column-1)
                    self.__cellCheck(row, column, row, column+1)
                else:
                    self.__grid[row][column] = self.new_cell_value
                    self.new_cell_value += 1

    #is site (row i, column j) open?
    def isOpen(self, row, column):
        if (row == (self.__rows - 1) or row == 0):
            return True

        if self.__grid[row][column] == ((self.__columns)*(row-1) +column+1):
            return False
        else:
            return True

    #is site (row i, column j) full?
    def isFull(self, row, column):
        if (row == (self.__rows - 1) or row == 0):
            return False

        if self.__grid[row][column] == ((self.__columns)*(row-1) +column+1):
            return True
        else:
            return False

    def __cellCheck(self, row, column, cell_row, cell_column):
        if(self.isOpen(cell_row, cell_column)):
            q = self.__grid[row][column]
            p = self.__grid[cell_row][cell_column]
            for row in range(self.__rows):
                for column in range(self.__columns):
                    if self.__grid[row][column] == p:
                        self.__grid[row][column] = q
        return

    #does the system percolate?
    def percolates(self):
        if (self.__grid[0][0] == self.__grid[self.__rows - 1][0]):
            return True
        else:
            return False
    def printGrid(self):
        print str(self.__grid)

grid = Percolation(results_int[0][0])

for element in range(1,len(results_int), 1):
    grid.Open(results_int[element][0], results_int[element][1] - 1)

print "Does the input perculate? " + str(grid.percolates())



