# Recursion Removal
- sometimes it works, sometimes it's very expensive. 
    - Tower of hanoi = very useful
    - Fibonacci = impractical after 50 or so values
    
## COUNTING PERMUTATIONS WITHOUT DUPES
Multiplying the number of choices at each step gives the total number of possible permutations

    EX: n x (n - 1) x (n - 2) x ... x (n - k + 1).
    
In special case where k = n (i..e you are generating permutations that select all N of the items w/o dupes)
the formula becomes n!. 

    n1 is the number that most people think of as the # of permutations in a set
    
    
## Tail Recursion
(See TailRecursion.java)
Why? 
- Since converting tail recursion to a loop is so straightforward, many compilers do this automatically 
to reduce stack space requirements of the application.

## Storing Intermediate Values(Memoization)
(See MemoizationFibonacci)
This is super fast, because rather than calculating every fibonacci every time we call the function, 
we store the values of each result. This allows us to search for the closest value and work from there, 
solving the problem almost instantly because we are keeping a table of x number of fibonaccis in memory.


## General Recursion Removal
- mimic what a program does when it performs the recursion

Before making a recursive call, a program stores information about
its current state on the stack. 
- when recursive call is made
    - state is popped off the call stack so that it can resume 
    execution where it left off.
    
### MIMICING
- divide an algorithm into sections that come before each recursive call
    - label these sections 1, 2, 3 etc.
- create a variable  SECTION
    - this should indicate which section the algorithm should execute next
- create a while (SECTION > 0) loop
    - put algo code inside the while loop and place it inside a
    series of if-else statements. 
    - each if statement  has to compare the variable  SECTION to a
    section and execute the corresponding code. 
    - NOTE (Switch Case is also relevant!)