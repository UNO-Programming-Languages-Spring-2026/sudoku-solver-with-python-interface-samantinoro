% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...

%subgrid is sqrt of full range
#const subgridsize = 3.
#const domain = subgridsize ** 2.

val(1..domain).

%for every cell, get 1 value
{ sudoku(R,C,V) : val(V) } = 1 :- val(R), val(C).

%initials
sudoku(R,C,V) :- initial(R,C,V).

%no repeat rows or columns
:- sudoku(R, C1, V), sudoku(R, C2, V), C1 != C2.
:- sudoku(R1, C, V), sudoku(R2, C, V), R1 != R2.

%subgrid divided by total size
%goes from 4 values to 3 as per instructions
%G calculations work by stratifying the rows, 1*3, 2*3, 3*3  + column modifier
subgrid(R,C,G) :- val(R), val(C), SR = (R-1) / subgridsize, SC = (C-1) / subgridsize, G = 1 + (SR * subgridsize + SC).

%subgrids can only have 1 of each value
%if not in same coords, cant be same value (if in same subgrid)
:- sudoku(R1, C1, V), sudoku(R2, C2, V), subgrid(R1, C1, G), subgrid(R2, C2, G), (R1, C1) != (R2, C2).

#show sudoku/3.