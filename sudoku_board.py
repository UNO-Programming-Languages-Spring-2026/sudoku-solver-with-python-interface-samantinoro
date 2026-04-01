from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE  - question 3

        #print(sorted(self.sudoku.items()))

        strlist = [ s[1] for s in sorted(self.sudoku.items())]

        #print(strlist)

        #every 27 is new row of blocks,
        #every 9 is new row
        #ever 3 is new col of blocks
        #ez pz
        for i in range(len(strlist)):
            if i == 0:
                pass
            elif i % 27 == 0:
                s += "\n\n"
            elif i % 9 == 0:
                s += "\n"
            elif i % 3 == 0:
                s += " "

            s += str(strlist[i]) + " "

        s += "\n"

        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE - quesiton 5

        #print(s)

        new_s = s.split()

        #print(new_s)

        newdict= {}

        #*kinda* like the opposite of __str__
        #takes from string, but excludes all '-'s
        #maps directly from long-ass string onto dict, 3x3x3 = 81 in sequence
        for i in range(9):
            for j in range(9):
                val = (i*9 +j)
                if new_s[val].isdigit():
                    newdict[(i+1,j+1)] = int(new_s[val])
                else:
                    pass

        sudoku = newdict

        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE - question 2

        #print(model.symbols(shown=True))

        #thre3_way_list = [[arg.number for arg in s.arguments] for s in model.symbols(shown=True)]
        #uses nesting dictionary to turn sudoku placement values into dict coords and keys w/  .number

        board = { (s.arguments[0].number, s.arguments[1].number): s.arguments[2].number
        for s in sorted(model.symbols(shown=True))  }

        #print(board)

        return cls(board)
