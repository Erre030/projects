%Description: This encoding, given a specific instance (grid of nodes,starting positions of elements, etc.), generates movements for robots with some constraints. 
%Each robot has assigned a class to it and has to sucessfully finish all jobs and operations that matches his class within a given time limit.
%Every solution is optimized in the way that each robot should do the fewest moves possible to complete all his jobs and operations.

%Notes:
% Input:
%   #const n: the time steps range from 0 to n
%   edge(N1,N2): there is an (undirected) edge between nodes N1 and N2
%   robot(R,C,N): robot R is of class C and starts at node N
%   job(J,C,D): job J is of class C and its deadline is D
%   operation(J,O,N): J's operation O takes place at node N (O >= 1)
%
% Output:
%   at(R,N,T): robot R is at node N at time step T
%   assign(R,J,P): assign to R the job J at position P (in the sequence of jobs assigned to R) (P >= 1)

time(0..n).

% Robot movement---------------------------------------------------------------------------------

% Undirected edge to bidirectional edge
edge(N1,N2) :- edge(N2,N1). 

% Initial state (position of robot on time stemp 0)
at(R, N, 0) :- robot(R, C, N).

% Generate either movement or no movement (from current node, move to another node,connected by an edge to the current node, or stay at current node).All this only can happen, when the time stamp is smaller than n.

{ at(R, N, T+1); at(R, N2, T+1) } :- at(R, N, T), edge(N,N2), T < n.

% There cannot be a time where there is no position / no location given for a robot 

:- time(T), not at(R, _, T), robot(R, _, _).

% A robot cannot be at two different nodes at the same time
:- at(R, N, T), at(R, N2, T), N != N2.

% Constraints that robot can only move to node if node is not occupied by another robot
:- at(R, N, T), at(R2, N, T), R != R2.

% Constraints that two robot cannot switch their nodes in the next time stamp
:- at(R, N, T), at(R2, N2, T), at(R, N2, T+1), at(R2, N, T+1), R != R2, N != N2.

% Assign job procedure--------------------------------------------------------------------------

% "Preassign" all jobs to each robot (for every job, which has the same class as a robot we create exactly one preassign atom with the value of the robot and its job)
1 { preassign(R, J) : robot(R, C, _) } 1 :- job(J, C, _).

% Count up all jobs possible for each robot (we create a total_preassign atom (T,R) where T counts all the cases where preassign (R,J) has the same R but different J's. 
%R is defined all the existing robots from the different classes.
%Counts values for all robots seperately, also if they are in the same class, cause we are using an individual R for every preassign.
%But one job may be assigned more than once to differnet robots of the same class)

total_preassigns(T, R) :- T = #count { J : preassign(R, J) }, robot(R , C, _).

% Assign each job to robot with help of total_preassigns (we build a new assign atom (R,J,P) , where for each robot (R) and job (J) of the same class one total_preassign (T) is picked for (P).
%This (P) is picked beginning at 1 and finishing at T, so we create a priority for each job. 
%(total_preassigns(T) encompasses all the jobs of one class)

1 { assign(R, J, P) : robot(R, C, _), job(J, C, _)} 1 :- total_preassigns(T,R), P = 1..T.

% Each robot can only have unique priorities for each job
:- assign(R, J, P), assign(R, J2, P), J != J2.

% There can only be one roboter for each job
:- assign(R, J, _), assign(R2, J, _), R != R2.

% "Robot tracking" / actions-------------------------------------------------------------------------

% If a robot R is at node N at time T, and R has an operation O of job J assigned at N, then R "performs" O. 
%(we are just linking the node where the robot is at with the node of the operation from the job of the robot by going into the job and adressing the parts of the specific operation atom for the job.)
%(We are using the body to create for every at-atom a perform operation atom, if the at-atom node matches the operation node.)

1 { perform_operation(R, J, O, T) : at(R, N, T)} 1 :- operation(J, O, N), assign(R, J, P).

% Jobs have to be performed within given job deadline
:- perform_operation(R, J, O, T), job(J, _, D), T > D.

% For a single robot, two operations cannot be completed in one time step (different operations of different jobs can't be done in a single time stamp)
:- perform_operation(R, J, O, T), perform_operation(R, J2, O2, T), (J,O) != (J2, O2).

% two different jobs with different priorization get assigned to one robot. Makes sure that jobs are completed by their prios (higher prio jobs have to be done before lower prior jobs).
%Also makes sure, that jobs can't be done simultaneously.
% A robot has to complete jobs in the right order
%a robot can't perform a job with lower priority at an earlier or the same time stamp than another job with higher priority.
%(the highest priority is 1, second highest priority = 2 , ...)

:- perform_operation(R, J, _, T), perform_operation(R, J2, _, T2), assign(R,J,P), assign(R,J2,P2), P > P2, T <= T2.

% Operations of the same job have to be performed in the correct order (operation with lower priority can't be performed before operation with higher priority)
%(the highest priority is 1, second highest priority = 2 , ...)

:- perform_operation(R, J, O, T), perform_operation(R, J, O2, T2), O < O2, T > T2.

% There can be no operation that hasn't been performed in the end (compare performed operations with not performed operation values)
:- operation(J, O, _), not perform_operation(_, J, O, _).


% Minimize / penalize node changes wrt R and T---------------------------------------------------------------------------------
%every time the robot moves/changes nodes, he gets a penalty of 1, the penalties will be incremented for every condition(in this case the condition is, that the robot moves/change nodes)

%minimize counts the condition presented  after the colon, starting with 1 for every robot at every time stamp.
% T and R (specifier) are included (1,T,R) because for every robot at every time stamp there should be an own minimize statement. 
%(If R wouldn't be included, we would only create one minimize statement, which encompasses all robots at once on every time stamp.)
%(same thing goes for T. If T wouldn't be included, we couldn't tell the time stamps apart and there would be one minimize statement for all time stamps together.)

#minimize{ 1, T, R : at(R, N, T), at(R, N2, T+1), N != N2 }. 


%
%
%
%#show time/1.
#show at/3.
#show assign/3.
%#show preassign/2.
%#show total_preassigns/2.
%#show edge/2.
%#show perform_operation/4.
%#show operation/3.
%#show job/3.