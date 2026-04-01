import sys, clingo
from sudoku_board import Sudoku


class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")

        input_str = ""

        for f in files:
            with open(f, 'r') as file:
                input_str += file.read()

        if not files:
            input_str = sys.stdin.read()

        board = Sudoku.from_str(input_str)
        ctx = Context(board)


        ctl.ground([("base", [])], context =ctx)

        ctl.solve()

    def print_model(self, model, printer) -> None:
        symbols = sorted(model.symbols(shown=True))

        #sys.stdout.write(" ".join(str(s) for s in symbols) + "\n")
        #sys.stdout.flush()

        sys.stdout.write(Sudoku.__str__(Sudoku.from_model(model)))
        sys.stdout.flush()


class Context:

    def __init__(self, board: Sudoku):
        self.board = board

    def initial(self) -> list[clingo.symbol.Symbol]:
        # YOUR CODE HERE

        touse = (self.board.sudoku.items())
        initials = [[s[0][0], s[0][1], s[1]] for s in touse]

        #print(initials)

        symbols = []

        #essentially reverse engineering from_model from sudoku_board
        for i in initials:
            s = clingo.Function("", [clingo.Number(i[0]), clingo.Number(i[1]), clingo.Number(i[2])])
            symbols.append(s)


        return symbols


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp(), sys.argv[1:])
