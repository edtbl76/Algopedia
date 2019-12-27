package Java.EssentialAlgorithms.Chapter10_Trees.BinaryTrees;

import java.util.LinkedList;

public class BinaryNode {

    private String name;
    private BinaryNode leftChild;
    private BinaryNode rightChild;

    public BinaryNode(String name) {
        this.name = name;
    }

    /*
        PREORDER TRAVERSAL:

            Root -> Left -> Right
     */
    public String preorder() {
        StringBuilder sb = new StringBuilder(name);
        if (leftChild != null)
            sb.append(" ").append(leftChild.preorder());
        if (rightChild != null)
            sb.append(" ").append(rightChild.preorder());
        return String.valueOf(sb);
    }

    /*
        INORDER TRAVERSAL:

            Left -> Root -> Right
     */
    public String inorder() {
        StringBuilder sb = new StringBuilder();
        if (leftChild != null)
            sb.append(" ").append(leftChild.inorder());

        sb.append(name);

        if (rightChild != null)
            sb.append(" ").append(rightChild.inorder());
        return String.valueOf(sb);
    }

    /*
        POSTORDER TRAVERSAL:

            Left -> Right -> Root
     */
    public String postorder() {
       StringBuilder sb = new StringBuilder();
        if (leftChild != null)
            sb.append(" ").append(leftChild.postorder());

        if (rightChild != null)
            sb.append(" ").append(rightChild.postorder());

        sb.append(name);
        return String.valueOf(sb);
    }

    /*
        Breadth First Traversal
     */
    public String breadthFirst() {
        StringBuilder sb = new StringBuilder();
        LinkedList<BinaryNode> kids = new LinkedList<>();
        kids.addFirst(this);

        while(kids.size() > 0) {
            BinaryNode node = kids.removeLast();
            sb.append(" ").append(node.name);

            if (node.leftChild != null)
                kids.addFirst(node.leftChild);
            if (node.rightChild != null)
                kids.addFirst(node.rightChild);
        }
        return String.valueOf(sb).stripLeading();
    }

    public void setLeftChild(BinaryNode leftChild) {
        this.leftChild = leftChild;
    }

    public void setRightChild(BinaryNode rightChild) {
        this.rightChild = rightChild;
    }
}
