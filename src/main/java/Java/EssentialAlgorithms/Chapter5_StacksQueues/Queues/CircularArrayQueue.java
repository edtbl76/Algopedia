package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues;

public class CircularArrayQueue<E> {
    private E[] values;
    private int next;
    private int last;
    private int size = 0;

    public CircularArrayQueue(int size) {
        this.values = (E[])new Object[size];
        this.next = 0;
        this.last = 0;
    }

    public int getNext() {
        return next;
    }

    public void setNext(int next) {
        this.next = next;
    }

    private int getLast() {
        return last;
    }

    private void setLast(int last) {
        this.last = last;
    }

    public void enqueue(E value) {
        // This is the difference between a circular and non circular queue
        int marker = (getNext() + 1) % this.values.length;
        if(marker == getLast())
            throw new ArrayIndexOutOfBoundsException();

        this.values[getNext()] = value;
        setNext(marker);
        size++;
    }

    public E dequeue() {
        if (getNext() == getLast())
            throw new ArrayIndexOutOfBoundsException();

        E result = values[getLast()];
        this.values[getLast()] = null;
        setLast((getLast() + 1) % this.values.length);
        size--;
        return result;
    }

    public int size() {
        return size;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();

        /**
         * This is a tricky little bitch.
         * - The iterator values are tied to the number of items in the Array when toString() is called.
         * - size() is my tracking variable to the current number of items.
         *
         *  To retain order I have to start w/ i = last (which is essentially my access pointer).
         *  However, last in this structure is circular, so once I hit my "bounds" I need it to wrap around.
         *  This is where we mod this.values.length, which allows us to cycle back around to get the values
         *  that have been inserted in circular fashion back at the beginning of the circular array.
         *
         */
        int i = last;
        for (int j = 1; j <= size; j++) {
            builder.append(values[i]).append(" ");

            /*
                i + 1 is the incr. operation.
                the mod operation ensures that the result of the incr doesn't result in a bounds violation.
             */
            i = (i + 1) % this.values.length;
        }
        return String.valueOf(builder).stripTrailing();
    }
}
