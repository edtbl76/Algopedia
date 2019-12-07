package Java.EssentialAlgorithms.Chapter6_Sorting.ON2;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;
import java.util.stream.IntStream;

public class BubbleSortExec2 {
    public static void main(String[] args) {
        int[] array = new int[7];
        populate(array, 7);

        System.out.println("Unsorted : " + Arrays.toString(array));
        sort(array);

    }

    private static void populate(int[] array, int max) {
        IntStream.rangeClosed(1, max).forEach(value -> {
            array[value - 1] = ExecUtils.getRandom(max, 1);
        });
    }

    private static void sort(int[] array) {

        /*
            Bounds Tracking.
            - these values allow us to "clip off" the ends of the array if they are already sorted.
            - this works w/ a back and forth traversal to "work towards the middle". We end up solving the
            problem in fewer traversals.

                ("Not all N are equal")
         */
        int min = 0;
        int max = array.length - 1;

        /*
            This is an accumulator for demonstrating how many iterations of the while loop we pass through to
            reach the solution.
         */
        int counter = 1;

        /*
            This is the logic loop for the sort algorithm. We will remain in this loop until the structure is sorted.
         */
        while (min < max) {

            /*
                Set last swapped to our lower bounds.
             */
            int last = min;

            System.out.println("===== Iteration #" + counter);
            System.out.println("  Min: " + min + " Max: " + max);

            /*
                Forward Pass:
                - iterate from min to max.
                - if the current element is greater than the next value, swap them.
                    - update the swap pointer to the current index (because a swap happened)
             */
            for (int i = min; i < max; i++) {

                if(array[i] > array[i + 1]) {

                    // Demo Print Statements
                    System.out.println("\tForward  (Pre) : " + Arrays.toString(array));
                    System.out.println("\t\tSwapping Best: " + array[i] + "[" + i + "] With: "
                            + array[i + 1] + "[" + (i + 1) + "]");

                    int temp = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = temp;

                    last = i;

                    // Demo Print Statements
                    System.out.println("\tForward  (Post): " + Arrays.toString(array));
                    System.out.println();
                }
            }

            /*
                Once the forward pass is complete, we set our new max bound to the last swapped index.
                (if no swaps occur beyond a given index, then the remaining elements "to the right" are already
                sorted)
             */
            max = last;
            System.out.println("  Min: " + min + " Max: " + max);

            /*
                This is the end condition for the loop. Once the bounds meet or contradict each other logically,
                the loop is complete.
             */
            if (min >= max)
                break;

            /*
                Set the swap pointer to our max bound (These are probably already equal, but whatever).
             */
            last = max;

            /*
                Backward Pass:
                    - here we are going to work down from the max to min bound.
                    - if the current element is less than the previous element swap them
                        - update the swap pointer if a swap happens
             */
            for (int i = max; i > min; i--) {
                if(array[i] < array[i - 1]) {

                    // Demo Print Statements
                    System.out.println("\tBackward (Pre) : " + Arrays.toString(array));
                    System.out.println("\t\tSwapping: " + array[i] + "[" + i + "] With Best: "
                            + array[i - 1] + "[" + (i - 1) + "]");

                    int temp = array[i];
                    array[i] = array[i - 1];
                    array[i - 1] = temp;

                    last = i;

                    // Demo Print Statements
                    System.out.println("\tBackward  (Post): " + Arrays.toString(array));
                    System.out.println();
                }
            }

            // After the pass set the new bounds.
            min = last;
            System.out.println("  Min: " + min + " Max: " + max);

            // Update demo counter to track iterations.
            counter++;


        }
    }


}
