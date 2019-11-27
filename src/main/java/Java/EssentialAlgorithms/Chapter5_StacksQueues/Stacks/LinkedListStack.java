package Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks;


public class LinkedListStack<E> {

    /**
     * FIELDS
     */

    private int size = 0;
    private Node<E> head;


    /**
     * CONSTRUCTORS
     */

    public LinkedListStack() {
        head = new Node<>();
    }

    public LinkedListStack(E data) {
        this();
        Node<E> node = new Node<>(data);
        head.setNext(node);
        size = 1;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void push(E data) {
        Node<E> node = new Node<>(data);
        node.setNext(head.getNext());
        head.setNext(node);
        size++;
    }

    public E pop() {
        if (head.getNext() == null)
            return null;
        else {
            E result = head.getNext().getData();
            head.setNext(head.getNext().getNext());
            size--;
            return result;
        }
    }


    /**
     * NODE
     */

    static class Node<E> {

        private E data;
        private Node<E> next;
        private boolean visited = false;

        Node() {}

        Node(E value) {
            this.data = value;
        }

        public E getData() {
            return data;
        }

        public void setData(E data) {
            this.data = data;
        }

        public Node<E> getNext() {
            return next;
        }

        public void setNext(Node<E> next) {
            this.next = next;
        }

        public boolean isVisited() {
            return visited;
        }

        public void visit() {
            visited = true;
        }

        public void unvisit() {
            visited = false;
        }

        @Override
        public String toString() {
            return String.valueOf(this.getData());
        }
    }
}
