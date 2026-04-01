from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE

        #print(sorted(self.sudoku.items()))

        strlist = [ s[1] for s in sorted(self.sudoku.items())]

        #print(strlist)

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

        #print(s)

        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE

        #print(model.symbols(shown=True))

        #3_way_list = [[arg.number for arg in s.arguments] for s in model.symbols(shown=True)]

        board = { (s.arguments[0].number, s.arguments[1].number): s.arguments[2].number
        for s in sorted(model.symbols(shown=True))  }

        #print(board)

        return cls(board)
