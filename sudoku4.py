import sys, clingo
from sudoku_board import Sudoku as sudoku


class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        ctl.load("sudoku.lp")

        for f in files:
            ctl.load(f)

        if not files:
            ctl.load("-")

        ctl.ground([("base", [])])

        ctl.solve()

    def print_model(self, model, printer) -> None:
        symbols = sorted(model.symbols(shown=True))

        #sys.stdout.write(" ".join(str(s) for s in symbols) + "\n")
        #sys.stdout.flush()

        #uses _str_ to take model and turn it into valid string  to display - q4
        sys.stdout.write(sudoku.__str__(sudoku.from_model(model)))
        sys.stdout.flush()


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp(), sys.argv[1:])
