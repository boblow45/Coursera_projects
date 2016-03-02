import sys

results = []
with open('input20.txt') as inputfile:
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

#print str(results_int) + "\n"

class FastCollinearPoints(object):
    def __init__(self, points):
        self.N = points[0][0]
        self.points = []
        self.linesegments = []
        for element in range(1, self.N+1):
            array = [points[element][0],points[element][1], None, []]
            self.points.append(array)


            # points is an array of arrays. The array inside the array is made up of the following way
            # [x-point, y-point, slope with respect to point of interest,[list of all slopes of lines which this point is part of]]
    def FastCollinearPoints(self):
        # Go through each set of x and y coordinate and calculate the slope with respect to the other given x and y coordinates
        for j in range(self.N):
            # if there are less than four points there can't be a straignt line of line 4 points or grear. Therefore,
            # break out of loop
            if (self.N - j) <3:
                break
            # Go through each set of x and y coordinates, calculate the slope with respect to that point and save the slope
            # with that set of x and y coordinates in the self.points[element][2] location
            for w in range(j+1, self.N):

                if self.points[w][0] - self.points[j][0] == 0:
                    slope = 9999999999999999999999999999
                else:
                    slope = (self.points[w][1] - self.points[j][1])/float(self.points[w][0] - self.points[j][0])

                self.points[w][2] = slope
            # sort the all points with respect to the slope

            self.sort(self.points[j+1:])
            self.points[j+1:] = self.aux


            print "arraies to search for a line: " + str(self.points[j+1:]) + "\n"
            # the folloing are required when trying to locate lines in the set of given x and y coordinates
            number_same_slope = 1
            pre_slope = None

            for element in range(j+1, self.N):

                #print number_same_slope
                #print "number_same_slope has a values of: " + str(number_same_slope)
                # if the current slow is different to previous point slope check reset counter for tracking point with the
                # same slope. if the counter is 3 or greater log that set of points if has not been already logged
                if pre_slope != self.points[element][2] or (element == (self.N-1)):
                    if (element == (self.N-1)):
                        number_same_slope += 1
                    # after sorting if there are three point one after the other with the same slope there is a straight
                    # line with at least four points. In this case we need to save this set of points.
                    if number_same_slope >= 3:
                        append_array = [[self.points[j][0],self.points[j][1]]]

                        points_Not_in_line = True
                        for x in range(element - number_same_slope, element , 1):
                            # the points array contains four elements. The array contains the x-coordinate, y-coordinate
                            # the slope with respect to the current point and the set of line slopes which containt this
                            # point. if the last element of the points array is empty then this point is part of no line.
                            # but if it part of a line the set of slopes in this array can be used to prevent the points
                            # being redocunment as part of a line.
                            for k in self.points[x][3]:
                                if k == pre_slope:
                                    points_Not_in_line = False
                            # if the slope is in the third element of the points array don't add the point to the list
                            # of lines as it has already be added.
                            if points_Not_in_line:
                                #following line of code appends the points if a line is created
                                append_array.append(self.points[x][0:2])
                                self.points[x][3].append(pre_slope)
                        # if the slope is in the third element of the points array don't add the point to the list
                        # of lines as it has already be added.
                        if points_Not_in_line:
                            self.linesegments.append(append_array)
                    number_same_slope = 1
                    pre_slope = self.points[element][2]
                    continue
                number_same_slope += 1

    def numberOfSegments(self):
        return len(self.linesegments)

    def Linesegment(self):
        return self.linesegments

    def sort(self, a):
        N = len(a)
        self.aux = [None]*N
        sz = 1
        sz_array = [1]
        lo_array = [0]

        for x in range(len(a)):
            #print element
            if sz < len(a):
                sz += sz
                sz_array.append(sz)
            else:
                break


            #if lo <
            # might need to replace the iner for loop.
            # it might be doing what it is bous to do

        for count in sz_array:
            for lo in range(0, N-count, count + count):
                self.__merge(a, lo, lo + count - 1, min(lo+count+count, N-1))
            #print str(self.aux) + "\n"
        #sys.exit(-1)
    def __merge(self, a, lo, mid, hi):
        print "lo has a value of: " +str(lo)
        print "mid has a value of: " +str(mid)
        print "hi has a value of: " +str(hi) + "\n"

        self.aux = a[:]

        i = lo; j = mid+1
        for k in range(lo, hi+1, 1):
            if (i > mid):
                a[k] = self.aux[j]
                j += 1
            elif (j > hi):
                a[k] = self.aux[i]
                i += 1
            elif(self.aux[j][2] < self.aux[i][2]):
                a[k] = self.aux[j]
                j += 1
            else:
                a[k] = self.aux[i]
                i += 1

test = FastCollinearPoints(results_int)
test.FastCollinearPoints()

array = test.Linesegment()
for element in range(len(array)):
    print ("line %d is made up of the following points" %element) + str(array[element])