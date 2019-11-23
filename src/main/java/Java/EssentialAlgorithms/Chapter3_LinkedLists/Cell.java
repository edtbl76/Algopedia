package Java.EssentialAlgorithms.Chapter3_LinkedLists;

public class Cell<E extends Comparable<E>> {

    public E data;
    public Cell<E> next;
    public Cell<E> prev;

    public Cell() { }

    public Cell(E data) {
        this.data = data;
    }

    /**
     * @return returns value of data
     */
    public E getData() {
        return data;
    }

    /**
     * @param data value of data stored in Cell
     */
    public void setData(E data) {
        this.data = data;
    }

    /**
     * @return pointer to next cell
     */
    public Cell<E> getNext() {
        return next;
    }

    /**
     * @param next Cell object of type E
     */
    public void setNext(Cell<E> next) {
        this.next = next;
    }

    /**
     * @return pointer to prev cell
     */
    public Cell<E> getPrev() {
        return prev;
    }

    /**
     * @param prev pointer to Cell of parameter type E
     */
    public void setPrev(Cell<E> prev) {
        this.prev = prev;
    }

    @Override
    public String toString() {
        return String.valueOf(getData());
    }


    public int compareTo(Cell<E> node) {
        int result = this.getData().compareTo(node.getData());
        return Integer.compare(result, 0);
    }
}
