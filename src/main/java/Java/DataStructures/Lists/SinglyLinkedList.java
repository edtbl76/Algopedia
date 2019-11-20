package Java.DataStructures.Lists;

/**
 * Standard LinkedList impl
 */
public class SinglyLinkedList {

    /**
     * First node of the list (nothing points to it)
     */
    private Node head;

    /**
     * no. of nodes
     */
    private int size;

    /**
     * Default Constructor is an empty head.
     */
    public SinglyLinkedList() {
        head = new Node(0);
        size = 0;
    }

    public SinglyLinkedList(Node head, int size) {
        this.head = head;
        this.size = size;
    }

    /**
     * Inserts element at head.
     * @param x Element to be added
     */
    public void insertHead(int x) {
        insertAt(x, 0);
    }

    /**
     * Inserts element at tail
     * @param data Element to be added
     */
    public void insert(int data) {
        insertAt(data, size);
    }

    /**
     * Inserts node at given position
     * @param data value to be stored.
     * @param position where to store it
     */
    public void insertAt(int data, int position) {
        // Make sure given position isn't stupid.
        checkListBounds(position, 0, size);

        // set current to existing head.
        Node current = head;

        // traverse list until we get to the position we are looking for
        for (int i = 0; i < position; i ++)
            current = current.getNext();

        // create a new node, initialized w/ the given data.
        Node node = new Node(data);

        /*
            Insertion logic.
            - current is the existing node.
            - set the new node's pointer to the existing node's pointer.
                (That node will be after our new node)
            - set the existing node's pointer to point to the new node
                (The existing node will be before our new node)
            - increment size of data structure.
         */
        node.setNext(current.getNext());
        current.setNext(node);
        size++;
    }

    /**
     * Insert that keeps the data sorted largest to smallest
     * @param data value to be inserted.
     */
    public void insertSorted(int data) {
        Node current = head;

        /*
            as long as the next value isn't null and our existing
            data is greater than the next value, keep going.
         */
        while (current.getNext()!= null && data > current.getNext().getValue()) {
            current = current.getNext();
        }

        /*
            Insertion logic
         */
        Node node = new Node(data);
        node.setNext(current.getNext());
        current.setNext(node);
        size++;
    }

    /**
     * Deletes the head object
     */
    public void deleteHead() {
        deleteAt(0);
    }

    /**
     * deletes the element at the tail.
     */
    public void delete() {
        deleteAt(size - 1);
    }

    /**
     * deletes an element at given position
     * @param position position in list to remove.
     */
    public void deleteAt(int position) {
        // make sure position isn't stupid
        checkListBounds(position, 0, size - 1);
        Node current = head;
        for (int i = 0; i < position; i++) {
            current = current.getNext();
        }

        /*
            Extraction logic.
            - set node to remove as the next node.
            - set the current pointer to the pointer of the next node
            - set node to remove to null.
            - decrement size of structure.
         */
        Node node = current.getNext();
        current.setNext(current.getNext().getNext());
        node = null;
        size--;
    }


    public void checkListBounds(int position, int low, int high) {
        if (position > high || position < low)
            throw new IndexOutOfBoundsException(position + "");
    }

    public void clear() {
        if (size == 0)
            return;
        Node prev = head.getNext();
        Node current = prev.getNext();

        while (current != null) {
            prev = null;
            prev = current;
            current = current.getNext();
        }
        prev = null;
        head.setNext(null);
        size = 0;
    }

    /**
     * @return true if list is empty
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * @return no. of nodes/elements in list.
     */
    public int size() {
        return size;
    }

    @Override
    public String toString() {
        if (size == 0)
            return "";

        StringBuilder list = new StringBuilder();
        Node current = head.getNext();
        while (current != null) {
            list.append(current.getValue()).append("->");
            current = current.getNext();
        }
        return list.replace(list.length() - 2, list.length(), "").toString();
    }

    public static SinglyLinkedList merge(SinglyLinkedList list1, SinglyLinkedList list2) {
        Node head1 = list1.head.getNext();
        Node head2 = list2.head.getNext();

        int size = list1.size() + list2.size();

        Node head = new Node();
        Node tail = head;
        while (head1 != null && head2 != null) {
            if (head1.getValue() <= head2.getValue()) {
                tail.setNext(head1);
                head1 = head1.getNext();
            } else {
                tail.setNext(head2);
                head2 = head2.getNext();
            }
            tail = tail.getNext();
        }

        if (head1 == null)
            tail.setNext(head2);
        if (head2 == null)
            tail.setNext(head1);

        return new SinglyLinkedList(head, size);
    }
}

/**
 * Node = entry of node.
 */
class Node {

    /**
     * value stored by the Node
     */
    int value;

    /**
     * pointer to then ext node
     */
    Node next;

    Node() {}

    Node(int value) {
        this(value, null);
    }

    Node(int value, Node next) {
        this.value = value;
        this.next = next;
    }

    public int getValue() {
        return value;
    }


    public void setValue(int value) {
        this.value = value;
    }

    public Node getNext() {
        return next;
    }

    public void setNext(Node next) {
        this.next = next;
    }
}