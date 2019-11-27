package Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks;

public class DoubleStack<E> {

    E[] values;
    private int nextTop;
    private int nextBottom;

    /*
        The push/pop methods for the top of the structure work the same.
        However, the pup/pop methods for the bottom of the structure work backwards, because we are working
        from the end of the array (where the index is the highest).
     */
    public DoubleStack(int size) {
        this.values = (E[])new Object[size];
        nextTop = 0;
        nextBottom = size - 1;
    }

    public void pushTop(E data) {
        if (nextTop > nextBottom)
            throw new IndexOutOfBoundsException();

        values[nextTop] = data;
        nextTop++;
    }

    public void pushBottom(E data) {
        if (nextTop > nextBottom)
            throw new IndexOutOfBoundsException();

        values[nextBottom] = data;
        nextBottom--;
    }

    public E popTop() {
        if (nextTop == 0)
            throw new IndexOutOfBoundsException();

        nextTop--;
        return values[nextTop];
    }

    public E popBottom() {
        if (nextBottom == values.length - 1)
            throw new IndexOutOfBoundsException();

        nextBottom++;
        return values[nextBottom];
    }

}
