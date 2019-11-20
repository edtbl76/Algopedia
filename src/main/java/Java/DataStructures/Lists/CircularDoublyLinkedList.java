package Java.DataStructures.Lists;

public class CircularDoublyLinkedList<E> {
    static class Node<E> {
        E data;
        Node<E> next;
        Node<E> prev;

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

        public Node<E> getPrev() {
            return prev;
        }

        public void setPrev(Node<E> prev) {
            this.prev = prev;
        }

        @Override
        public String toString() {
            return String.valueOf(getData());
        }
    }

    private int size = 0;
    private Node<E> head = null;
    private Node<E> tail = null;

    public int size() {
        return size;
    }

    public Node<E> getHead() {
        return head;
    }

    public Node<E> getTail() {
        return tail;
    }

    public void insertAtHead(E data) {
        Node<E> node = new Node<>(data);
        // If size is 0, then set the node to head and close the loop
        if (isEmpty()) {
            head = node;
            tail = node;
            head.setNext(head);
            head.setPrev(head);
        } else {
            Node<E> temp = head;
            node.setNext(temp);
            temp.setPrev(node);
            node.setPrev(tail);
            head = node;
            tail.setNext(head);
        }
        size++;
    }

    public void insertAtTail(E data) {
        Node<E> node = new Node<>(data);
        if (isEmpty()) {
            head = node;
            tail = node;
            head.setNext(head);
            head.setPrev(head);
        } else {
            Node<E> temp = tail;
            node.setNext(head);
            node.setPrev(temp);
            head.setPrev(node);
            temp.setNext(node);
            tail = node;
        }
        size++;

    }

    public void _deleteSingle() {
        head.setNext(null);
        head.setPrev(null);
        tail.setNext(null);
        tail.setPrev(null);
        size = 0;
    }

    public void deleteHead() {
        if (!isEmpty()) {
            if (size == 1) {
                _deleteSingle();
            } else {
                head.getNext().setPrev(tail);
                tail.setNext(head.getNext());
                head = head.getNext();
                size--;
            }
        }
    }

    public void deleteTail() {
        if (!isEmpty()) {
            if (size == 1) {
                _deleteSingle();
            } else {
                tail.getPrev().setNext(head);
                head.setPrev(tail.getPrev());
                tail = tail.getPrev();
                size--;
            }
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

    public E get(int position, boolean reversed){
        if (reversed) {
            if (position <= size) {
                Node<E> node = tail;
                while (position - 1 != 0) {
                    node = node.getPrev();
                    position--;
                }
                return node.getData();
            } else {
                throw new IndexOutOfBoundsException();
            }
        } else {
            return get(position);
        }
    }

    public boolean isEmpty() {
        return size == 0;
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

    public void clear() {
        while(!isEmpty()) {
            deleteHead();
        }
    }

    public String reversed() {
        StringBuilder list = new StringBuilder();
        Node<E> temp = tail;
        if (!isEmpty()) {
            do {
                list.append(temp.getData()).append("->");
                temp = temp.getPrev();
            } while (temp != tail);
        }
        return String.valueOf(list);
    }
}
