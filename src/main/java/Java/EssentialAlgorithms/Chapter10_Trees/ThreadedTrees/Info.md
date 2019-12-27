# Threaded Treees
THREAD 
- a series of links that allow you to move through the nodes in a tree or 
network in a way other than by following normal branches or links. 

THREADED TREE
- a tree that contains one or more threads.

BENEFITS:
- allow inorder/reverse traversal more quickly than is possible by using 
branches alone.

## SYMMETRICAL THREADED TREE
includes threads forward and backward through tree's INORDER traversal

## BUILDING THREADED TREES!

### CASE 1 (LEFT CHILD)
- The new node must be SMALLER than its parent
    - (Parent's Left Branch points to child)
    - new node left thread -> parent's left thread target
    - parent's left thread ->  null
    - new node right thread -> parent

### CASE 2 (RIGHT CHILD)
- the new node must be LARGER than its parent
    - (Parent's Right branch points to child)
    - new node right thread ->  parent's right thread target
    - parent's right thread -> null
    - new node left thread -> parent

## THREADED TREE TRAVERSAL
1. start at root node
2. set branch/thread toggle to TRUE
    - true = traversal by branch
    - false = traversal by thread
3. repeat algo while there are nodes to process
4. If toggle is TRUE 
    - move to the leftmost node and process it
5. If there is NO right branch
    - move to right thread
    - disable toggle
    - process node
6. If there is a right branch
    - move to right branch
    - then move down to the leftmost child of that node
    - process node.
