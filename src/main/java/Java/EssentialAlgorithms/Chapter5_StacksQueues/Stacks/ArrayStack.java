package Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks;

import java.util.Arrays;

public class ArrayStack<T> {

    private T[] values;
    private int next_index = 0;

    @SuppressWarnings("unchecked")
    public ArrayStack(int size) {
        this.values = (T[])new Object[size];
    }

    public void push(T value) {
        if (next_index == values.length) {
            throw new ArrayIndexOutOfBoundsException();
        } else {
           values[next_index] = value;
           next_index++;
        }
    }

    public T pop() {
        if (next_index == 0)
            throw new ArrayIndexOutOfBoundsException();
        else {
            /*
                This trick allows us to save some cycles by not deleting
                the value stored.
                - we simply decrement the insertion pointer and return the value at the current "next index"
                - The next time we perform a push, it will overwrite this value.
             */
            next_index--;
            return values[next_index];
        }
    }

    @Override
    public String toString() {
        return Arrays.toString(values);
    }
}
