package Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks;

import java.util.Stack;

public class StackSorter<E extends Comparable<? super E>> {

    private Stack<E> temp;
    private Stack<E> stack;

    public StackSorter() {
        temp = new Stack<>();
    }
    public StackSorter(Stack<E> stack) {
        this();
        this.stack = stack;
    }

    // ==== Methods

    /**
     * The basis of insertionSort is like sorting a deck of cards.
     * If we consider the cards in our hand from left to right, we start the process by taking the second
     * card from the left and "inserting" it into the proper order.
     * We move one card to the right each time, while the growing "hand" to the left is the sorted result.
     */
    public void insertionSort() {
        int size = stack.size();

        for (int i = 0; i < size; i++) {
            // first item
            E next = stack.pop();

            // dump everything to temp
            for (int j = 0; j  < size - i - 1; j++) {
                temp.push(stack.pop());
            }

            // eval
            while (stack.size() > 0) {
                E test = stack.pop();
                if (test.compareTo(next) >= 0) {
                    stack.push(test);
                    break;
                }
                temp.push(test);
            }
            // add next at this position
            stack.push(next);

            // DEMO OUTPUT ONLY
            System.out.println("\tSortedSoFar: " + stack + " / " + temp);

            // move remaining back on original list.
            while (temp.size() > 0)
                stack.push(temp.pop());

        }
    }

    /**
     * Selection sort is another way of "card sorting"
     * In this manner, we "select" the largest item in the deck and move it all the way to the left, then we move the
     * next largest item to the right of it, and so on, until the cards are ordered from greatest to lowest (left to
     * right)
     */
    public void selectionSort() {
        int size = stack.size();
        int sorted = 0;
        int unsorted = size;

        for (int i = 0; i < size; i++) {

            /*
                Find item belongs in position i

                Pull first item off stack as "biggest so far"
             */
            E biggest = stack.pop();

            // move other items into temp stack (track largest)
            for (int j = 0; j < unsorted - 1; j++) {
                E test = stack.pop();
                if (test.compareTo(biggest) > 0) {

                    // move old biggest to temp, and replace it w/ new
                    temp.push(biggest);
                    biggest = test;
                } else {

                    // if not bigger, just move it to temp
                    temp.push(test);
                }
            }
            // biggest at this point belongs at position i
            stack.push(biggest);

            // DEMO PURPOSES ONLY
            System.out.println("\tSortedSoFar: " + stack + " / " + temp);

            // move unsorted items back to stack.
            while (temp.size() > 0) {
                stack.push(temp.pop());
            }

            // update accumulators
            sorted++;
            unsorted--;
        }
    }

}
