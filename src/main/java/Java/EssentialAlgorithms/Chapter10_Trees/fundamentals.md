# Tree Fundamentals
highly RECURSIVE data structures used to store HIERARCHICAL data and model decison making processes that 
consists of nodes and branches
- usually branches (between nodes) are DIRECTED to define a parent-child relationship
    - NOTE: arrows go FROM parent TO child
- SIBLINGS are nodes that share the same parent. (this is kind of obvious)
- DESCENDANTS are the nodes DOWN the tree
- ANCESTORS are relative nodes UP the tree

## TREE CHARACTERISTICS
Degree is the maximum number of children a node has. 
- EX: a binary tree allows each node to have 2 children

LEAF (a.k.a. External Node)
- node with no children

INTERNAL NODE
- a node w/ at least one child.

LEVEL/DEPTH
- the distance from a given node to the root (the first node)
- EX: the root's level is 0

HEIGHT
- length of the longest path from a node to the bottom of the tree (i.e. to a leaf node)

SUBTREE
- if tree T has a node called R, then the subtree at that node is R and all of its descendants

ORDERED TREE
- a tree created in such a manner that the sequence oof the children is significant

UNORDERED TREE
- kids are all over the place! Don't matter none!

FIRST COMMON ANCESTOR(or LEAST COMMON ANCESTOR)
- for any two nodes, this is the closest ancestor to BOTH nodes.
    - (In some cases, this is one of the nodes, i.e. for a parent child relationship.)
    
"UNIQUE PATH"
- there is a unique path between ANY TWO NODES in a tree that doesn't cross any branch more than once.

FULL TREE
- every node either has zero kids, or it has the full degree of kids

COMPLETE TREE
- every level is completely full, except possibly the bottom level, where all the nodes are pushed as far left as
possible.

PERFECT TREE
- full, and all leaves are at the same level
- i.e. tree holds every possible node for a tree of its height.

## PROPERTIES OF BINARY TREES
Number of Branches
- number of branches (B) in a binary tree w/ N nodes
    - (B = N - 1)
    
    
    EX:
       10 - 1 = 9
       10 nodes, has 9 branches  
    
Number of Nodes
- number of nodes (N) in a perfect Binary Tree of Height H is
    - (N = 2^(H+1) - 1)
    
    
    EX:
        Height = 2
        2^(2 + 1) - 1 = 2^(3) - 1 = 8 - 1 = 7
        A Perfect Binary Tree with a Height of 2 has 7 nodes
        
Height
- if a perfect binary tree has N nodes, it has a height of 
    - LOG(2)(N + 1) - 1
    
    
    EX:
        N = 7
        LOG(2)(7 + 1) - 1
        LOG(2)(8) - 1           
        3 - 1 = 2. 
        
LEAF NODES
- the # of leaf nodes (L) in a perfect binary tree of height (H) is
    - (L = 2^(H))
    
    
    EXAMPLE
        IF I have a HEIGHT of 2, then I have 
        2^2 = 4 LEAF NODES
        
    
INTERNAL NODES
- in a perfect binary tree, there is one more leaf than internal node
    - (I = L - 1)


    PROOF
        Total Number of Nodes (N)in Perfect Binary Tree (of Height H) 
        = 2^(H + 1) - 1
        
        Internal nodes (I) = N - L
            or
            
        =   2^(H + 1) - 1 - (2^(H))
        =   (2^(H + 1) - 2^(H)) - 1
        =   2^(H) * (2 - 1) - 1
        =   2^(H) * 1 - 1
        =   2^H - 1
        
        FOR A Height of 2,
        we have internal nodoes of 2^2 - 1 = 4 - 1 = 3. 
        

        
        
       
        
        
                        
    
    