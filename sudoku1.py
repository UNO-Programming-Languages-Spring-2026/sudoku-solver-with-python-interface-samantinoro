import sys, clingo


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

        #basically from slides, except do standard output instead of print
        #Q1
        sys.stdout.write(" ".join(str(s) for s in symbols) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp(), sys.argv[1:])
