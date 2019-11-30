package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues;

public class LinkedListDeque<E> {

    private Node<E> head;
    private Node<E> tail;

    /**
     * Main constructor builds the head and tail, and then links them.
     */
    public LinkedListDeque() {
        head = new Node<>();
        tail = new Node<>();

        head.setNext(tail);
        tail.setPrev(head);
    }

    /**
     * enqueue operation by default will behave like a normal queue.
     * providing a boolean of false can enqueue at the tail.
     */
    public void enqueue(E data) {
        Node<E> node = new Node<>(data);
        enqueueHead(node);
    }

    public void enqueue(E data, boolean head) {
        Node<E> node = new Node<>(data);
        if (head)
            enqueueHead(node);
        else
            enqueueTail(node);
    }


    private void enqueueHead(Node<E> node) {
                                            // head ---> head.next
                                            // head <--- head.next
        node.setNext(head.getNext());       // head, node --> head.next  (head.next becomes node.next)
        node.getNext().setPrev(node);       // head, node <--- node.next
        node.setPrev(head);                 // head <--- node
        head.setNext(node);                 // head ---> node
    }

    private void enqueueTail(Node<E> node) {
                                            // tail.prev ---> tail
                                            // tail.prev <--- tail
        node.setPrev(tail.getPrev());       // tail.prev <--- node, tail  (tail.prev becomes node.prev)
        node.getPrev().setNext(node);       // node.prev ---> node, tail
        node.setNext(tail);                 // node      ---> tail
        tail.setPrev(node);                 // node      <--- tail
    }

    /**
     * Default operation is to return from tail.
     */
    public E dequeue() {
        return dequeueTail();
    }

    /**
     * Overloaded method supports a boolean allowing to select between head/tail.
     */
    public E dequeue(boolean tail) {
        if (tail)
            return dequeueTail();
        else
            return dequeueHead();
    }

    private E dequeueHead() {
        if (head.getNext() == tail)
            return null;

        Node<E> temp = head.getNext();          // head --> head.next  (head.next becomes temp)
        head.setNext(temp.getNext());           // head --> head.next.next, temp  (head.next.next becomes new head.next)
        head.getNext().setPrev(head);           // head <-- head.next
        return temp.getData();
    }

    private E dequeueTail() {
        if (tail.getPrev() == head)
            return null;

        Node<E> temp = tail.getPrev();          // tail.prev <-- tail   (tail.prev becomes temp)
        tail.setPrev(temp.getPrev());           // tail.prev.prev <-- tail (tail.prev.prev becomes tail.prev)
        tail.getPrev().setNext(tail);           // tail.prev --> tail
        return temp.getData();
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

        Node(E data) {
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

        Node<E> getPrev() {
            return prev;
        }

        void setPrev(Node<E> prev) {
            this.prev = prev;
        }

        @Override
        public String toString() {
            return String.valueOf(this.getData());
        }
    }
}
