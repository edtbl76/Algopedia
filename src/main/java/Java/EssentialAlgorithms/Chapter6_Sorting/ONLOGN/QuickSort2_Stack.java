package Java.EssentialAlgorithms.Chapter6_Sorting.ONLOGN;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;
import java.util.Stack;
import java.util.stream.IntStream;

public class QuickSort2_Stack {
    public static void main(String[] args) {
        int[] array = populate(10);
        System.out.println("Initial Array: " + Arrays.toString(array));
        sort(array);
        System.out.println("Sorted Array: " + Arrays.toString(array));
    }

    /**
     * QuickSort Stack
     * - I overload this to make life easier.
     * - we need the start/end created externally to sort, so if we create a version that takes just the array, we
     *  can use it to extract start/end values and then do the needful.
     *
     *  NOTE: this is almost identical
     */
    private static void sort(int[] values) {
        sort(values, 0, values.length - 1, 1);
    }

    private static void sort(int[] values, int start, int end, int counter) {


        // make sure we have something to sort!
        if(start >= end) {
            System.out.println("\tNothingToSort: " + Arrays.toString(values) + " (" + start + "," + end + ")");
            return;
        }
        System.out.print("\tSorting: " + Arrays.toString(values) + " (" + start + "," + end + ")");

        // set sort marker at the beginning (this is arbitrary).
        int marker = values[start];
        System.out.println(" Around: " + marker);

        // Create stacks for before/after the marker
        Stack<Integer> less = new Stack<>();
        Stack<Integer> greater = new Stack<>();

        // populate stacks relative to the value at the marker
        for (int i = start + 1; i <= end; i++) {
            if(values[i] < marker)
                less.push(values[i]);
            else
                greater.push(values[i]);
        }

        /**
         * Here we are taking the values less than marker and putting them back into our array
         */
        System.out.println("\t<  : " + less);
        int index = start;
        while (less.size() > 0) {
            values[index] = less.pop();
            index++;
        }

        /**
            Adding the divider back into the structure is important, because it preserves the parts of the
            final result that are already sorted

            we store the index as midpoint and then increment it. The incr is to ensure that the value at index isn't
            shared by the two stacks.
         */
        values[index] = marker;
        int midpoint = index;
        index++;

        /**
         * Here we are taking the values greater than the marker and putting them back into our array
         */
        System.out.println("\t>= : " + greater);
        while (greater.size() > 0) {
            values[index] = greater.pop();
            index++;
        }

        // sort the two halves
        System.out.println("Iteration: === " + counter + " ===");
        counter++;
        sort(values, start, midpoint - 1, counter);
        sort(values, midpoint + 1, end, counter);
    }

    private static int[] populate(int max) {
        int[] array = new int[max];
        IntStream.rangeClosed(1, max).forEach(value -> array[value - 1] = ExecUtils.getRandom(max, 1));

        return array;
    }
}
