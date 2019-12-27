package Java.EssentialAlgorithms.Chapter10_Trees.ThreadedTrees;


public class ThreadedNode {

    private Integer value;
    private ThreadedNode leftChild;
    private ThreadedNode rightChild;
    private ThreadedNode leftThread;
    private ThreadedNode rightThread;

    ThreadedNode() {}

    public ThreadedNode(Integer value) {
        this.value = value;
    }

    public ThreadedNode getLeftChild() {
        return leftChild;
    }

    public ThreadedNode getRightChild() {
        return rightChild;
    }

    public ThreadedNode getLeftThread() {
        return leftThread;
    }

    public ThreadedNode getRightThread() {
        return rightThread;
    }

    public int getValue() {
        return value;
    }

    public void addNode(Integer value) {

        if (this.value == null) {
            this.value = value;
            return;
        }

        if (value < this.value) {
            if (leftChild != null)
                leftChild.addNode(value);
            else {

                ThreadedNode child = new ThreadedNode(value);
                child.leftThread = this.leftThread;
                child.rightThread = this;
                this.leftChild = child;
                this.leftThread = null;
            }
        } else {
            if (rightChild != null)
                rightChild.addNode(value);
            else {
                ThreadedNode child = new ThreadedNode(value);
                child.leftThread = this;
                child.rightThread = this.rightThread;
                this.rightChild = child;
                this.rightThread = null;
            }
        }
    }




}
