
%Description: A sudoku solver which solves every typical sudoku given a certain instance



% generator------------------------------------------------------------------------------------------

#const n=9.

row (1..n).
col(1..n).
numbers(1..n).
subgrid_size(3).

% generate candidates:
{sudoku(I,J,N) : row(I),col(J),numbers(N)} = n*n.


% transform initial values to sudoku values:
sudoku(I,J,N) :- initial(I,J,N).

   
%tester-----------------------------------------------------------------------------------------------------

% same col:
:- sudoku(I,J,N), sudoku(I',J,N), I != I'.

% same row:                          
:-sudoku(I,J,N), sudoku(I, J', N), J!= J'.
                      
% you can exactly choose one number for every cell:
1{sudoku(I,J,N) : numbers(N)}1 :-row(I),col(J).                        
                            
                                                                                                              
% build and constraints for subgrids:
                        
%get index values for subgrids:                             
subgrid(I,J,M) :-row(I),col(J), M = (((I-1)/S)*S + (J-1)/S), subgrid_size(S).
                                        
%exclude equal numbers in sudoku if their subgrid index is the same                                             
:- sudoku(I,J,N), sudoku(I',J',N), subgrid(I,J,M), subgrid(I',J',M), I != I', J != J'.


#show sudoku/3.