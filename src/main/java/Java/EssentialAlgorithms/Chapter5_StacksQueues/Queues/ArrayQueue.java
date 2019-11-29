package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues;


public class ArrayQueue<E> {

    private E[] values;
    private int next;
    private int last;
    private int size = 0;

    public ArrayQueue(int size) {
        this.values = (E[])new Object[size];
        this.next = 0;
        this.last = 0;
    }

    public void enqueue(E value) {
        int marker = next + 1;
        if(marker == last)
            throw new ArrayIndexOutOfBoundsException();

        this.values[next] = value;
        this.next = marker;
        size++;
    }

    public E dequeue() {
        if (next == last)
            throw new ArrayIndexOutOfBoundsException();

        E result = values[last];
        this.values[last] = null;
        this.last = last + 1;
        size--;
        return result;
    }

    public int size() {
        return size;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (int i = last; i < values.length; i++) {
            builder.append(values[i]).append(" ");
        }
        return String.valueOf(builder).stripTrailing();
    }
}
