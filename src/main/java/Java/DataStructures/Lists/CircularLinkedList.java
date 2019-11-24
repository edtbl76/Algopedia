package Java.DataStructures.Lists;

import java.util.List;

public class CircularLinkedList<E> {
    public <T> CircularLinkedList(List<T> asList) {
    }

    static class Node<E>  {
        E data;
        Node<E> next;

        public Node() {}

        public Node(E data) {
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

        @Override
        public String toString() {
            return String.valueOf(getData());
        }
    }

    private int size = 0;
    public Node<E> head = null;
    public Node<E> tail = null;

    public CircularLinkedList() { }

    public void insert(E data) {
        Node<E> node = new Node<>(data);
        // If size is 0, then set the node to head and close the loop
        if (isEmpty()) {
            head = node;
            tail = node;
            head.setNext(head);
        } else {
            Node<E> temp = head;
            node.setNext(temp);
            head = node;
            tail.setNext(head);
        }
        size++;
    }

    public int size() {
        return size;
    }

    public void append(E data) {
        if(isEmpty()) {
            insert(data);
        } else {
            Node<E> node = new Node<>(data);
            tail.setNext(node);
            tail = node;
            tail.setNext(head);
            size++;
        }
    }

    public void delete() {
        if (!isEmpty()) {
            head = head.getNext();
            tail.setNext(head);
            size --;
        }
    }

    public E get(int position) {

        if (position <= size) {
            Node<E> node = head;
            while (position - 1 != 0) {
                node = node.getNext();
                position--;
            }
            return node.getData();
        } else {
            throw new IndexOutOfBoundsException();
        }
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public void clear() {
        while(!isEmpty()) {
            delete();
        }
    }

    @Override
    public String toString() {
        StringBuilder list = new StringBuilder();
        Node<E> temp = head;
        if(!isEmpty()) {
            do {
               list.append(temp.getData()).append("->");
               temp = temp.getNext();
            } while (temp != head);
        }

        return String.valueOf(list);
    }
}
