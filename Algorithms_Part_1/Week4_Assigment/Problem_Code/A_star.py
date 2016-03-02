class Board(object):
    def __init__(self, blocks):               # construct a board from an N-by-N array of blocks
        pass                            # (where blocks[i][j] = block in row i, column j)

    def dimension(self):                # board dimension N
        pass

    def hamming(self):                  # number of blocks out of place
        pass

    def manhattan(self):                # sum of Manhattan distances between blocks and goal
        pass

    def isGoal(self):                   # is this board the goal board?
        pass

    def twin(self):                     # a board that is obtained by exchanging any pair of blocks
        pass

    def equals(self, y):                # does this board equal y?
        pass

    def neighbors(self):                # all neighboring boards
        pass

    def toString(self):                 # string representation of this board (in the output format specified below)
        pass


#The following class will inhert from the revious class and I need to make a prity queue of object of type board
class Solver(Board):
    def __init__(self, InitialBoard):               # find a solution to the initial board (using the A* algorithm). This will set up a board using the super function
        # Call the Parent classes constructor
        super(Solver, self).__init__(InitialBoard)
        pass

    def isSolvable(self):                           # is the initial board solvable?
        pass

    def moves(self):                                # min number of moves to solve initial board; -1 if unsolvable
        pass

    def solution(self):                             # sequence of boards in a shortest solution; null if unsolvable
        pass

    def main(args):                                 # solve a slider puzzle (given below)
        pass