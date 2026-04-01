%given this:
%sudoku(R,C,V) :- initial(R,C,V).


%python linker
initial(R, C,V) :- (R, C, V) = @initial().

sudoku(R, C, V) :- initial(R, C, V).


