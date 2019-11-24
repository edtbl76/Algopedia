package Java.EssentialAlgorithms.Chapter3_LinkedLists;

import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

public class DoublyLinkedListImpl<E extends Comparable<E>>  {

    private int size = 0;
    private Cell<E> head;
    private Cell<E> tail;

    // =======  Constructors

    public DoublyLinkedListImpl() {
        head = new Cell<>();
        tail = new Cell<>();
    }

    public DoublyLinkedListImpl(List<E> c) {
        head = new Cell<>();
        tail = new Cell<>();
        /*
            Cheap short cut to guarantee existing order of the list.
         */
        for (int i = 0; i < c.size(); i++) {
            insertAtTail(c.get(i));
        }
    }

    // =======  Helpers.

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        Cell<E> node = head;
        while (node.getNext() != null && node.getNext() != tail) {
            /*
                This space is just a hand-wave for demo purposes. I would probably use String.join() or
                Apache Commons StringUtils() to create a more flexible implementation (so we can let the user
                decide how it will be printer based on the args)
             */
            builder.append(node.getNext()).append(" ");
            node = node.getNext();
        }
        // This is just an el-cheapo way of cleaning up that loose space at the end of the string.
        return String.valueOf(builder).stripTrailing();
    }

    // ======= INSERTION

    public void insertAtHead(E data) {
        Cell<E> node = new Cell<>(data);


        if (isEmpty()) {
            head.setNext(node);
            node.setNext(tail);
            tail.setPrev(node);
            node.setPrev(head);
        } else {
            Cell<E> temp = head.getNext();

            head.setNext(node);
            node.setNext(temp);
            node.setPrev(head);
            temp.setPrev(node);
        }
        size++;
    }

    public void insertAtTail(E data) {
        Cell<E> node = new Cell<>(data);

        if (isEmpty()) {
            tail.setPrev(node);
            node.setPrev(head);
            head.setNext(node);
            node.setNext(tail);
        } else {
            Cell<E> temp = tail.getPrev();
            tail.setPrev(node);
            node.setPrev(temp);
            temp.setNext(node);
            node.setNext(tail);
        }
        size++;
    }

    public void insertAfter(E target, E data) {
        if (isEmpty())
            insertAtHead(data);
        else {
            Cell<E> found = get(target);
            if (found == null)
                return;

            Cell<E> node = new Cell<>(data);
            if (found.getNext() == tail)
                insertAtTail(data);
            else {
                node.setNext(found.getNext());
                found.getNext().setPrev(node);
                node.setPrev(found);
                found.setNext(node);
                size++;
            }
        }
    }

    public void insertBefore(E target, E data) {
        if (isEmpty())
            insertAtTail(data);
        else {
            Cell<E> found = get(target, true);
            if (found == null)
                return;

            Cell<E> node = new Cell<>(data);
            if (found.getPrev() == head)
                insertAtHead(data);
             else {
                 node.setPrev(found.getPrev());
                 found.getPrev().setNext(node);
                 node.setNext(found);
                 found.setPrev(node);
                 size++;
            }
        }
    }

    public void insertSorted(E data) {
        // If it's empty, insert it at the top.
        if (isEmpty()) {
            insertAtHead(data);
            return;
        }

        // create our node and then a moving pointer to the head.
        Cell<E> node = new Cell<>(data);
        Cell<E> current = head;

        /*
            Stop when we hit the tail.
            - use our comparator to compare the "next" value w/ our argument data. we need it to iter through

            if the current value is < argument, we keep iterating.
            EX: our first value in DDLImplExec2 is 5. This gets inserted at the top (because we start empty)
            Our second value is 1. 5 > 1, so the loop is never evaluated, so current is the head.
            Our third value is 7, which means we get to the end of the loop.

         */
        while((current.getNext() != tail) && (current.getNext().getData().compareTo(node.getData()) < 0)) {
            current = current.getNext();
        }
        node.setNext(current.getNext());
        current.setNext(node);
        node.setPrev(current);
        current.getNext().setPrev(node);
        size++;
    }

    // =========== SORTING
    public DoublyLinkedListImpl<E> selectionSort() {
        DoublyLinkedListImpl<E> sorted = new DoublyLinkedListImpl<>();

        // set current to the first element of THIS list.
        Cell<E> current = head;

        // No nulls or tail.
        while (current.getNext() != null && current.getNext() != tail) {

            /*
                before_best is the cell before the largest value.
                best_value is the best_value.
                best is the "best cell"
             */
            Cell<E> before_best = current;
            E best_value = before_best.getNext().getData();
            Cell<E> best = current;

            // best is the "best so far" It's really just a pointer to current.
            while (best.getNext() != null && best.getNext() != tail) {

                /*
                    This updates our new best_value field, based on comparator.
                    - this also updates before_best, because it only changes when best_value does.
                 */
                if (best.getNext().getData().compareTo(best_value) > 0) {
                    before_best= best;
                    best_value = before_best.getNext().getData();
                }
                best = best.getNext();

            }
            /*
                If we get this far, we have the best value. Swapping in place is possible but hard to track.
                (personally... one solution in a DLL is to  insert the new values at the tail and put a marker in front
                of the new value that blocks the while loops from continuing. However, this might break the other
                insertion logic.
             */
            delete(best_value);
            sorted.insertAtHead(best_value);

        }
        return sorted;
    }

    // ========== COPYING

    /**
     * Demos DLLImplExec4. - Kind of straight forward. Some of these work by returning just the sentinel, and
     * tracking what's been added.
     *
     * In this case, I built a new list here. and insertAtTail the data.
     */
    public DoublyLinkedListImpl<E> copy() {
        DoublyLinkedListImpl<E> copyList = new DoublyLinkedListImpl<>();
        Cell<E> last_added = copyList.head;

        Cell<E> current = head.getNext();
        while (current != tail) {
            last_added = current;
            copyList.insertAtTail(last_added.getData());
            current = current.getNext();
        }
        last_added.setNext(tail);
        return copyList;
    }


    // ========= DELETE
    public void deleteAtHead() {
        if (isEmpty())
            return;

        if (size == 1) {
            clear();
            return;
        }

        Cell<E> temp = head.getNext().getNext();
        head.setNext(temp);
        temp.setPrev(head);
        size--;
    }

    public void deleteAtTail() {
        if (isEmpty())
            return;

        if (size == 1) {
            clear();
            return;
        }

        Cell<E> temp = tail.getPrev().getPrev();
        tail.setPrev(temp);
        temp.setNext(tail);
        size--;
    }

    public void delete(E target) {
        if (isEmpty())
            return;

        if (size == 1) {
            clear();
            return;
        }

        Cell<E> found = get(target);
        if (head.equals(found)) {
            deleteAtHead();
        } else if (tail.equals(found)) {
            deleteAtTail();
        } else {
            Cell<E> after = found.getNext();
            Cell<E> before = found.getPrev();
            after.setPrev(before);
            before.setNext(after);
            size--;
        }

    }

    public void clear() {
        head.setNext(tail);
        tail.setPrev(head);
        size = 0;
    }

    // ========= FIND
    public Cell<E> get(E data) {
        if (isEmpty())
            return null;

        Cell<E> current = head.getNext();
        while (current != tail) {
            if (current.getData().equals(data))
                return current;
            current = current.getNext();
        }
        return null;
    }

    public Cell<E> get(E data, boolean reverse) {
        if (!reverse)
            return get(data);
        if (isEmpty())
            return null;

        Cell<E> current = tail.getPrev();
        while  (current != head) {
            if (current.getData().equals(data))
                return current;
            current = current.getPrev();
        }
        return null;


    }

    // ======= ITERATORS


    /**
     * This is for DDLImplyExec5
     * @return
     */
    public Iterator<E> iterator() {
        return new DoublyLinkedListIterator();
    }


    class DoublyLinkedListIterator implements Iterator<E> {

        private Cell<E> current;

        public DoublyLinkedListIterator() {
            // Skip head Sentinel
            current = head.getNext();
        }

        public E next() {
            if (current == null)
                throw new NoSuchElementException();

            E temp = current.getData();
            current = current.getNext();
            return temp;
        }

        public boolean hasNext() {
            // Stop before we hit the tail sentinel.
            return current != tail;
        }

        @Override
        public void remove() {
            delete(current.getData());
        }
    }
}
