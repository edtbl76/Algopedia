package Java.EssentialAlgorithms.Chapter6_Sorting.ONLOGN;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;
import java.util.stream.IntStream;

public class QuickSort3_InPlace {

    public static void main(String[] args) {
        int[] array = populate(10);
        System.out.println("Initial Array: " + Arrays.toString(array));
        sort(array);
        System.out.println("Sorted Array: " + Arrays.toString(array));
    }

    /**
     * QuickSort In Place
     * - I overload this to make life easier.
     * - we need the start/end created externally to sort, so if we create a version that takes just the array, we
     *  can use it to extract start/end values and then do the needful.
     *
     *  NOTE: This is typically the preferred method of doing this.
     */
    private static void sort(int[] values) {
        sort(values, 0, values.length -1, 1);
    }

    private static void sort(int[] values, int start, int end, int counter) {

        /*
            Evaluate if there is anything that needs sorting.
         */
        if (start >= end) {
            System.out.println("\tSortComplete: " + Arrays.toString(values) + " (" + start + "," + end + ")");
            return;
        }
        System.out.print("\tSorting: " + Arrays.toString(values) + " (" + start + "," + end + ")");


        // set our marker arbitrarily as the first value in the given array
        int marker = values[start];
        System.out.println(" Around: " + marker);

        /**
         * In Place logic.
         * - move items < marker to front of array
         * - move items >= marker to end of the array
         */
        int low = start;
        int high = end;
        for (;;) {


            /**
             * Work down from high to the marker.
             */
            while (values[high] >= marker) {
                high--;
                if(high <= low)
                    break;
            }
            // once high hits low, we need to reset the marker for "low"
            if (high <= low) {
                values[low] = marker;
                break;
            }

            // If we found a value, move it down to the lower half.
            System.out.println("\tMovingDown: " + values[high]);
            values[low] = values[high];
            System.out.println("\t\tWorkedDown: " + Arrays.toString(values));

            /**
             * work up from low to marker
             */
            while (values[low] < marker) {
                low++;
                if(low >= high)
                    break;
            }

            // once low hits high, reset the marker for "high" and break out
            if (low >= high) {
                low = high;
                values[high] = marker;
                break;
            }

            // move any values up to high
            values[high] = values[low];
            System.out.println("\tMovinOnUp: " + values[low]);
            System.out.println("\t\tWorkedUp: " + Arrays.toString(values));

        }
        // recurse!
        System.out.println("Iteration: === " + counter + " ===");
        counter++;
        sort(values, start, low - 1, counter);
        sort(values, low + 1, end, counter);

    }

    private static int[] populate(int max) {
        int[] array = new int[max];
        IntStream.rangeClosed(1, max).forEach(value -> array[value - 1] = ExecUtils.getRandom(max, 1));

        return array;
    }
}
