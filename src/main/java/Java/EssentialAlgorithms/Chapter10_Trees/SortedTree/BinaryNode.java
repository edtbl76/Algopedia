package Java.EssentialAlgorithms.Chapter10_Trees.SortedTree;

import java.util.LinkedList;

public class BinaryNode {

    private Integer value;
    private BinaryNode left;
    private BinaryNode right;

    public BinaryNode() {}

    public BinaryNode(Integer value) {
        this();
        this.value = value;
    }

    public void add(Integer value) {

        // This allows us to use the default constructor without having to actually worry about NPE
        // Used Integer so we don't have to figure out how to
        // handle the valid case of '0'
        if (this.value == null) {
            this.value = value;
            return;
        }

        // If smaller, go down the left branch, if larger go down the right branch.
        if (value < this.value) {
            if (left == null) {
                System.out.println("Left - " + value);
                left = new BinaryNode(value);
            } else {
                left.add(value);
            }
        } else {
            if (right == null) {
                right = new BinaryNode(value);
                System.out.println("Right - " + value);
            } else {
                right.add(value);
            }
        }
    }

    public BinaryNode find(Integer value) {
        if (value.equals(this.value)) {
            return this;
        }

        if (value < this.value) {
            if (left == null) {
                return null;
            }
            return left.find(value);
        } else {
            if (right == null) {
                return null;
            }
            return right.find(value);
        }
    }

    public String breadthFirst() {
        StringBuilder sb = new StringBuilder();
        LinkedList<BinaryNode> kids = new LinkedList<>();
        kids.addFirst(this);

        while(kids.size() > 0) {
            BinaryNode node = kids.removeLast();
            sb.append(" ").append(node.value);

            if (node.left != null)
                kids.addFirst(node.left);
            if (node.right != null)
                kids.addFirst(node.right);
        }
        return String.valueOf(sb).stripLeading();
    }
}
