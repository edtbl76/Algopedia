package Java.EssentialAlgorithms.Chapter3_LinkedLists;

import java.util.List;

public class LinkedListSentinelImpl<E extends Comparable<E>> {

    private int size = 0;
    private Cell<E> head;

    public LinkedListSentinelImpl() {
        head = new Cell<>();
    }

    /**
     * This constructor is added for LLImplExec5
     */
    public LinkedListSentinelImpl(E data) {
        head = new Cell<>();
        Cell<E> node = new Cell<>(data);
        head.setNext(node);
        size = 1;
    }

    /**
     * This constructor is added for convenience for LLImplExec6 and on
     */
    public LinkedListSentinelImpl(List<E> c)  {
        head = new Cell<>();
        for (int i = 0; i < c.size(); i++) {
            insert(i, c.get(i));
        }
    }

    /**
     * returns size of LL. Note that this does NOT include the empty sentinel.
     */
    public int size() {
        return size;
    }

    /**
     * true if empty. Note, Sentinel doesn't count.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /*
        There are five types of insertions here:
        1.) insertion at the head relies on the sentinel being the first element.
        2.) insertion at the tail keeps going until we hit null.
        3.) insertion at a point  is basically pretending to be an array, by referencing the position in the list where
            i want to create the Cell.
        4.) insertAfter. This really relies on our use of next()
        5.) Before... yep  we just replace findCell() w/ findCellBefore()
     */
    /**
       Demonstrates inserting at the head of the data structure (LLImplExec5)
     */
    public void insertAtHead(E data) {
        Cell<E> node = new Cell<>(data);
        Cell<E> temp = head.getNext();
        head.setNext(node);
        node.setNext(temp);
        size++;
    }

    /**
     * Demonstrates insertion at the tail of the data structure (LLImplExec7)
     */
    public void insertAtTail(E data) {
        Cell<E> current = head;
        // Run until we get to the last element
        while(current.getNext() != null) {
            current = current.getNext();
        }

        Cell<E> node = new Cell<>(data);
        current.setNext(node);
        node.setNext(null);
        size++;
    }

    /**
     *
     * Demonstrates Inserting at given position (LLImplExec8)
     */
    public void insert(int position, E data) {

        if(isEmpty()) {
            insertAtHead(data);
        } else if(position == size) {
            insertAtTail(data);
        } else {
            Cell<E> current = head.getNext();
            for (int i = 1; i < position; i++) {
                current = current.getNext();
            }
            Cell <E> node = new Cell<>(data);
            node.setNext(current.getNext());
            current.setNext(node);
            size++;
        }
    }

    /**
     *  This is for LLImplExec9. We're kind of getting contrived here.
     *      This logic is only kind of useful, because if we have duplicate entries, do we want to keep searching?
     *
     */
    public void insertAfter(E target, E data) {

        if (isEmpty()) {
            insertAtHead(data);
            return;
        }
        Cell<E> found = findCell(target);
        insertByValue(data, found);
    }

    /**
     * This is for LLImplExec9. While this is contrived, I wanted to demonstrate the more realistic approach of
     * searching LLs by Value and then performing operations. This accentuates the cost of traversal.
     */
    public void insertBefore(E target, E data) {

        if (isEmpty()) {
            insertAtHead(data);
            return;
        }
        Cell<E> found = findCellBefore(target);
        insertByValue(data, found);
    }

    /**
     * This is just helper code. By combining this method w/ findCell() and findCellBefore() we can
     * easily create insertBefore() and insertAfter() circumstances.
     */
    private void insertByValue(E data, Cell<E> found) {
        if (found == null)
            return;

        Cell<E> node = new Cell<>(data);
        if (found.getNext() == null) {
            insertAtTail(data);
        } else {
            node.setNext(found.getNext());
            found.setNext(node);
            size++;
        }
    }

    /**
     * demonstrate LLImplExec10
     */
    public void deleteAtHead() {
        if (isEmpty())
            return;
        if (size == 1) {
            head.setNext(null);
        } else {
            head.setNext(head.getNext().getNext());
        }
        size --;

    }

    /**
     * demonstrate LLImplExec10
     */
    public void deleteAtTail() {
        if (isEmpty()) {
            return;
        }
        if (size == 1) {
            clear();
            return;
        }

        Cell<E> current = head;
        while(current.getNext().getNext() != null) {
            current = current.getNext();
        }
        current.setNext(null);

        size--;
    }

    /**
     * Demonstrate LLImplExec10
     */
    public void delete(int position) {

        if (isEmpty() || position > size)
            return;

        if (size == 1) {
            clear();
            return;
        }

        if (position == size) {
            deleteAtTail();
            return;
        }

        Cell<E> current = head;
        for (int i = 0; i < position; i++) {
            current = current.getNext();
        }
        Cell<E> temp = current.getNext();
        current.setNext(current.getNext().getNext());
        temp.setNext(current);
        size--;
    }

    public void clear() {
        head.setNext(null);
        size = 0;
    }


    /**
     * Deletion demo in LLImplExec10
     */
    public void deleteAfter(E target) {
        if (isEmpty()) {
            return;
        }

        if (size == 1) {
            head.setNext(null);
            size--;
        }

        Cell<E> found = findCell(target);
        if (found == null)
            return;

        if (found.getNext() != null) {
            Cell<E> temp = found.getNext();
            found.setNext(found.getNext().getNext());
            temp.setNext(found);
            size--;
        } else {
            deleteAtTail();
        }
    }

    /**
        Demonstrates the ability to find a Cell (by data) LLImplExec9
     */
    public Cell<E> findCell(E data) {
        if (isEmpty())
            return null;
        Cell<E> temp = head.getNext();
        while (temp != null) {
            if(temp.getData() == data) {
                return temp;
            }
            temp = temp.getNext();
        }
        return null;
    }

    public Cell<E> findCellBefore(E data) {
        Cell<E> node = head;
        while (node.getNext() != null) {
            /*
                Important. You can't use == to compare these. equals() is used for value comparison.
                == is used if they point to the same memory location.
             */
            if (node.getNext().getData().equals(data)) {
                return node;
            }
            node = node.getNext();
        }
        return null;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        Cell<E> node = head;
        while (node.getNext() != null) {
            if (node.getNext().getData() != null) {
                /*
                    This space is just a hand-wave for demo purposes. I would probably use String.join() or
                    Apache Commons StringUtils() to create a more flexible implementation (so we can let the user
                    decide how it will be printer based on the args)
                 */
                builder.append(node.getNext()).append(" ");
                node = node.getNext();
            }
        }
        // This is just an el-cheapo way of cleaning up that loose space at the end of the string.
        return String.valueOf(builder).stripTrailing();
    }
}
