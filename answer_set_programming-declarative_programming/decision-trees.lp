
%Description: This encoding, given a specific instance, generates binary decision trees, which correctly classify examples as positive or negative 
%while simultaneously stating, which features every specific example encompasses/not encompasses.

nodes(1..n).
edge(1,2).
edge(1,3).

% Generate candidates
{edge(X,Y) : nodes(X), nodes(Y)} = n-1. %always one edge less than nodes.

%CONSTRAIN CANDIDATES----------------------------------------------------------------------------

% Eliminate all edges where parent node X is bigger or equal to child node Y.
:- edge(X,Y), X >= Y. 
   
% Every node can not have more than two childs   
:- 3 {edge(X,Y) : nodes(Y)}, nodes(X).
    
% Every node can not have exactly one child
:- 1 {edge(X,Y) : nodes(Y)}1 , nodes(X).
    
% Eliminates all solutions where Y+1 != Y' if Y < Y' (ensure consecutive numbers as childs)
:- edge(X,Y), edge(X,Y'), Y < Y', Y' != Y + 1.

% Another parent can't have the same child    
:- edge(X,Y), edge(X',Y), X != X'.
                   
% Compare two edges and delete them if parent (X < X') but child of X is bigger than child of X'.                  
:- edge(X,Y), edge(X',Y'), X < X', Y > Y'.
                                                  
%GENERATING DECISION---------------------------------------------------------------------------------------
                   
% Extract attribute
attributes(A):- holds(X,A).
                   
% Generate exactly one decision for every interior nodes (with outgoing edges)             
1 {decision(N,A) : attributes(A)} 1 :- nodes(N),edge(N,Y).                                                                                                                                          
                                 
%PATH TRACING ----------------------------------------------------------------------------------------------------------
                                                          
% Extract example
examplenum(E):- example(E,C).                                

% Root node / base case (where the path starts)
subpath(1,E) :- examplenum(E).                                  

% Subpath direction of bigger child
subpath(N',E) :- subpath(N,E),edge(N,N'), decision(N,A),holds(E,A),edge(N,N'),edge(N,N''), N' > N''.      

% Subpath direction of smaller child
subpath(N'',E) :- subpath(N,E),edge(N,N'), decision(N,A),not holds(E,A),edge(N,N'),edge(N,N''), N' > N''.      

%CONSTRAINTS PATH TRACING-------------------------------------------------------------------------------------------------              

% Select nodes with no edges out (leafs)
leaf(N) :- nodes(N), 0 {edge(N,Y) : nodes(Y)} 0.      

% For bigger and smaller child choose either exactly one positive or negative
1{positive(N) ; negative(N)}1:- leaf(N),edge(X,N),edge(X,N'), N > N'. 
1{negative(N) ; positive(N)}1:- leaf(N),edge(X,N),edge(X,N'), N < N'.
      
% Delete all example classes that do not match with leaf node value
:-example(E,pos),leaf(N),subpath(N,E),negative(N).         
:-example(E,neg),leaf(N),subpath(N,E),positive(N).        
         

#show decision/2.
#show positive/1. 
#show edge/2. 