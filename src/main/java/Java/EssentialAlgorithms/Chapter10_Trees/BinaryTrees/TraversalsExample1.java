package Java.EssentialAlgorithms.Chapter10_Trees.BinaryTrees;

public class TraversalsExample1 {

    //Build BinaryNodes
    static BinaryNode root = new BinaryNode("E");
    static BinaryNode nodeA = new BinaryNode("A");
    static BinaryNode nodeB = new BinaryNode("B");
    static BinaryNode nodeC = new BinaryNode("C");
    static BinaryNode nodeD = new BinaryNode("D");
    static BinaryNode nodeF = new BinaryNode("F");
    static BinaryNode nodeG = new BinaryNode("G");
    static BinaryNode nodeH = new BinaryNode("H");
    static BinaryNode nodeI = new BinaryNode("I");
    static BinaryNode nodeJ = new BinaryNode("J");

    public static void main(String[] args) {

        // Link"em
        linkNodes();

        // Traverse!
        System.out.println("Preorder    : " + root.preorder());
        System.out.println("Inorder     : " + root.inorder());          // Symmetric Traversal
        System.out.println("Postorder   : " + root.postorder());
        System.out.println("BreadthFirst  : " + root.breadthFirst());
    }

    static void linkNodes() {

        /*
                            E
                     /              \
                    B               F
                 /      \              \
                A       D               I
                       /              /     \
                      C              G      J
                                       \
                                       H

         */

        root.setLeftChild(nodeB);
        root.setRightChild(nodeF);

        nodeB.setLeftChild(nodeA);
        nodeB.setRightChild(nodeD);

        nodeD.setLeftChild(nodeC);

        nodeF.setRightChild(nodeI);

        nodeI.setLeftChild(nodeG);
        nodeI.setRightChild(nodeJ);

        nodeG.setRightChild(nodeH);


    }
}

/*
    EXPLAIN OUTPUT

    PREORDER   (Root -> Left -> Right)

    (Root E)    Move Left to B
    (Root B)    Move Left to A
    (Root A)    LEAF, Up to B, Move Right to D
    (Root D)    Move left to C
    (Root C)    Unwind back to E, Move Right to F
    (Root F)    Move Right to I
    (Root I)    Move Left to G
    (Root G)    Move Right to H
    (Root H)    Unwind to I, Move Right to J
    (Root J)    Fini

    INORDER     (Left -> Root -> Right)

    -           Start at E, Left to B, Left A (Leaf)
    (Left A)    Up to B  (Root)
    (Root B)    Right to D, Left to C (Leaf)
    (Left C)    Up to D (Root)
    (Root D)    Unwind to E (Root)
    (Root E)    Right to F (Right)
    (Right F)   Right to I, Left to G (Left)
    (Left G)    Right to H (Leaf)
    (Right H)   Unwind to I (Root)
    (Root I)    Right to J (Leaf)
    (Right J)   Fini

    POSTORDER   (Left -> Right -> Root)

    -           Start at E, Left to B, Left A (Leaf)
    (Left A)    Up to B, Right to D, Left to C (Leaf)
    (Left C)    Up to D, (Root)
    (Root D)    Up to B, (Root)
    (Root B)    Up to E, Right to F, Right to I, Left to G, Right to H (Leaf)
    (Right H)   Up to G (Root)
    (Root G)    Up to I, Right to J (Right)
    (Right J)   Up to I, (Root)
    (Root I)    Up to F, (Root)
    (Root F)    Up to E, (Root)
    (Root E)    Fini

    Breadth First   ( Degree first)

    (E)         First
    (B)         Second
    (F)
    (A)         Third
    (D)
    (I)
    (C)         Fourth
    (G)
    (J)
    (H)         Fifth

 */
