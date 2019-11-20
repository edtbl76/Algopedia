package Java.DataStructures.Lists;

public class DoublyLinkedList {

    /**
     * front
     */
    private Link head;

    /**
     * back
     */
    private Link tail;

    public DoublyLinkedList() {
        head = null;
        tail = null;
    }

    /**
     * insert Data at front
     * @param data value to be stored
     */
    public void insertHead(int data) {
        // create a new element
        Link link = new Link(data);

        /*
            If the list is empty, then the new element is tail
            otherwise... set "previous" for current head to the element we are inserting
         */
        if(isEmpty()) {
            tail = link;
        } else {
            head.setPrevious(link);
        }
        /*
            set the next value for our new structure to be the "current head"
            then set our new element to be head.
         */
        link.setNext(head);
        head = link;
    }

    /**
     * Insert at the back
     * @param data value to be stored
     */
    public void insertTail(int data) {
        Link link = new Link(data);

        // no matter what, if we insert at tail, our next should be null
        link.setNext(null);

        if (isEmpty()) {
            tail = link;
            head = tail;
        } else {
            tail.setNext(link);
            link.setPrevious(tail);
            tail = link;
        }
    }

    /**
     * delete at front
     * @return Element deleted
     */
    public Link deleteHead() {
        // Store the existing head, so we can return it.
        Link temp = head;

        // set existing head to te next value.
        head = head.getNext();
        // Set the previous pointer to the new head. This removes all refs from old head, so it gets gc'd.
        head.setPrevious(null);

        // handle case of last record.
        if (head == null)
            tail = null;
        return temp;
    }

    /**
     * delete at tail
     * @return Element removed
     */
    public Link deleteTail() {
        Link temp = tail;
        tail = tail.getPrevious();
        tail.setNext(null);
        if (tail == null)
            head = null;
        return temp;
    }

    /**
     * delete given value
     * @param value value to be removed
     */
    public void delete(int value) {
        Link current = head;

        while(current.getValue() != value) {
            if (current != tail) {
                current = current.getNext();
            } else {
                System.out.println(value + " not found");
            }
        }

        if (current == head)
            deleteHead();
        else if (current == tail)
            deleteTail();
        else {
            /*
                remove pointers to current.
                - current's previous should skip current (so it points to current.next)
                - currents next should skip current (so it points to current's previous0
             */
            current.getPrevious().setNext(current.getNext());
            current.getNext().setPrevious(current.getPrevious());
        }
    }

    /**
     * inserts data, retains value ordering (high to low)
     * @param data value to be stored
     */
    public void insertOrdered(int data) {
        Link node = new Link(data);
        Link current = head;

        // traversal
        while (current != null && data > current.getValue() )
            current = current.getNext();

        if (current == head)
            insertHead(data);
        else if (current == null)
            insertTail(data);
        else {
            /*
                pointer management
                - new node is being inserted in front of "current" node

                - new node's previous should be set to current node's previous
                - current's previous should point at new node next
                - node's next should point to current
                - current's previous should point to new node.
             */
            node.setPrevious(current.getPrevious());
            current.getPrevious().setNext(node);
            node.setNext(current);
            current.setPrevious(node);
        }
    }

    /**
     * @return true if list is empty
     */
    public boolean isEmpty() {
        return (head == null);
    }

    @Override
    public String toString() {
        Link current = head;
        StringBuilder display = new StringBuilder();
        while (current != null) {
            display.append(current.toString()).append("->");
            current = current.getNext();
        }
        return display.toString();
    }

    public void clear() {
        if (isEmpty())
            return;
        Link prev = head.getNext();
        Link current = prev.getNext();

        while (current != null) {
            prev = null;
            prev = current;
            current = current.getNext();
        }
        prev = null;
        head.setNext(null);
    }
}

class Link {

    private int value;

    private Link next;
    private Link previous;

    public Link(int value) {
        this.value = value;
    }

    public Link getNext() {
        return next;
    }

    public void setNext(Link next) {
        this.next = next;
    }

    public Link getPrevious() {
        return previous;
    }

    public void setPrevious(Link previous) {
        this.previous = previous;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return String.valueOf(getValue());
    }
}
