package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues;

public class LinkedListQueue<E> {

    private int size = 0;
    private Node<E> head;
    private Node<E> tail;

    public LinkedListQueue() {
        head = new Node<>();
        tail = new Node<>();
    }

    public LinkedListQueue(E data) {
        this();
        Node<E> node = new Node<>(data);

        head.setNext(node);
        node.setNext(tail);

        tail.setPrev(node);
        node.setPrev(head);
        size = 1;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void enqueue(E value) {
        Node<E> node = new Node<>(value);

        /*
            If Structure is empty, next element after insertion is tail.

            Otherwise next element is head.getNext()
         */
        if (isEmpty()) {
            node.setNext(tail);
            tail.setPrev(node);
        } else {
            node.setNext(head.getNext());
            head.getNext().setPrev(node);
        }

        // Inserting new element after head and incrementing size happens regardless of other elements.
        head.setNext(node);
        node.setPrev(head);
        size++;
    }

    public E dequeue() {
        // if empty return null.
        if (isEmpty())
            return null;

        /*
            Store result, remove it from queue and then return and decr.
         */
        E result = tail.getPrev().getData();
        tail.setPrev(tail.getPrev().getPrev());
        tail.getPrev().setNext(tail);
        size--;

        return result;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        Node<E> current = head;
        while(current.getNext() != tail) {
            current = current.getNext();
            builder.append(current.getData()).append(" ");
        }
        return String.valueOf(builder);
    }

    static class Node<E> {

       private E data;
       private Node<E> next;
       private Node<E> prev;

       Node() {}

       public Node(E data) {
           this();
           this.data = data;
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

       public Node<E> getPrev() {
           return prev;
       }

       public void setPrev(Node<E> prev) {
           this.prev = prev;
       }

        @Override
        public String toString() {
           return String.valueOf(this.getData());
        }
    }

}
