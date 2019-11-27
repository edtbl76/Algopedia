package Java.EssentialAlgorithms.Chapter3_LinkedLists;

import java.util.List;

public class CircularLinkedListImpl<E> {

    /**
     * This is not a circular linked list.
     */
    private int size = 0;
    private Node<E> head;

    public CircularLinkedListImpl() {
        head = new Node<>();
    }

    public CircularLinkedListImpl(List<E> list) {
       this();
       for (int i = 0; i < list.size(); i++) {
            add(list.get(i));
       }
    }

    // ======  INSERTION CODE
    public void add(E value) {
        Node<E> node = new Node<>(value);
        node.setNext(null);

        if (isEmpty()) {
            head.setNext(node);
        } else {

            Node<E> temp = head.getNext();
            while (temp.getNext() != null) {
                temp = temp.getNext();
            }
            temp.setNext(node);
        }
        size++;
    }

    public void add(int index, E value) {
        //System.out.println(index + " " + size);
        Node<E> node = new Node<>(value);
        if(isEmpty()) {
            head.setNext(node);
            node.setNext(null);

        } else {
            /**
             * This has to be > (but not >=)
             * Even though we are treating this as a zero-based array w/ the positional add(), providing a value
             * of size() would be inserting a new element at the end.
             *
             *  i.e. if I have an existing List w/ 4 elements, they are numbered, 0-3. If I  supply 4 as the index,
             *  it is the same as calling add(E value)
             */
            if (index > size)
                throw new IndexOutOfBoundsException();

            Node<E> current = head;
            /**
             * If I pass in index 0, I want to insert it at the head
             *  - that means the loop doesn't execute, so current has to = head.
             */
            for (int i = 0; i < index; i++) {
                current = current.getNext();
            }
            node.setNext(current.getNext());
            current.setNext(node);
        }
        size++;
    }

    public void addFirst(E value) {
        Node<E> node = new Node<>(value);

        if (head.getNext() == null) {
            node.setNext(null);
        } else {
            node.setNext(head.getNext());
        }
        head.setNext(node);
        size++;
    }

    public void addLast(E value) {
        add(value);
    }


    // ====== DELETION
    public void clear() {
        head.setNext(null);
        size = 0;
    }

    public E remove(int index) {
        if(isEmpty())
            return null;

        if (index >= size)
            throw new IndexOutOfBoundsException();

        Node<E> current = head;
        for(int i = 0; i < index;i++) {
            current = current.getNext();
        }
        E saved = current.getNext().getData();
        current.setNext(current.getNext().getNext());
        size--;
        return saved;
    }


    // ====== RETRIEVE
    public boolean contains(E element) {
        Node<E> current= head;
        while(current.getNext() != null) {
            if (current.getNext().getData().equals(element))
                return true;
            current = current.getNext();
        }
        return false;
    }

    public E getFirst() {
        if (isEmpty())
            return null;

        return head.getNext().getData();
    }

    public E getLast() {
        if(isEmpty())
            return null;
        Node<E> current = head;
        while (current.getNext() != null) {
            current = current.getNext();
        }
        return current.getData();
    }

    public E get(int index) {

        if (isEmpty())
            return null;

        if (index >= size)
            throw new IndexOutOfBoundsException();

        /**
         * This works different than insertion. When we are inserting at a position, it means we are pushing an
         * existing piece of data forward one spot, so we are in that "findBefore" case.
         *
         * Here, we want EXACTLY what is at the given position
         */
        Node<E> current = head.getNext();
        for(int i = 0; i < index;i++) {
            current = current.getNext();
        }
        return current.getData();

    }

    public int indexOf(E element) {
        if(isEmpty())
            return -1;

        Node<E> current = head;
        int counter = 0;
        while(current.getNext() != null) {
            if (current.getNext().getData().equals(element))
                return counter;
            counter++;
            current = current.getNext();
        }

        return -1;
    }


    // ======  HELPERS

    public Node<E> getHead() {
        return head;
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * This is demonstrating how to check for a loop (CCLImplExec3).
     * NOTE: this may be unrealistic. In most cases, you aren't going to be able to insert flags into the objects
     * (nor would you want to!!!)
     */
    public boolean isLoop() {
        boolean hasLoop = false;

        Node<E> current = head;

        while(current.getNext() != null) {

            if(current.getNext().isVisited()) {
                current.setNext(null);
                hasLoop = true;
                break;
            }
            current = current.getNext();
            current.visit();
        }
        clearLoopFlags();
        return hasLoop;
    }

    public boolean hasLoopRetracing() {
        Node<E> node = head;
        while (node.getNext() != null) {
            Node<E> tracer = head;
            while(tracer != node) {
                if (tracer.getNext().equals(node.getNext())) {
                    // This is the loop. Break it!
                    node.setNext(null);
                    return true;
                }
                tracer = tracer.getNext();
            }
            node = node.getNext();
        }
        return false;
    }

    private void clearLoopFlags() {
        Node<E> current = head;
        while(current.getNext() != null) {
            current.unvisit();;
            current = current.getNext();
        }
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        Node<E> node = head;
        while (node.getNext() != null) {
            builder.append(node.getNext()).append(" ");
            node = node.getNext();
        }
        return String.valueOf(builder).stripTrailing();
    }

    /**
        Just a standard SinglyLinkedList Node impl.
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
