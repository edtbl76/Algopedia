package Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils;

public class Node {

    private int key;
    private String value;
    private Node next;

    public Node(int key, String value, Node next) {
        this.key = key;
        this.value = value;
        this.next = next;
    }


    public int getKey() {
        return key;
    }

    public void setKey(int key) {
        this.key = key;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public Node getNext() {
        return next;
    }

    public void setNext(Node next) {
        this.next = next;
    }

    @Override
    public String toString() {
        return "(" + key + ":" + value + ")";
    }
}
