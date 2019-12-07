package Java.EssentialAlgorithms.Chapter6_Sorting.ON;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;
import java.util.stream.IntStream;

public class CountingSort {

    public static void main(String[] args) {
        int max = 10;
        int[] array = populate(max);
        System.out.println("Initial Array: " + Arrays.toString(array));
        sort(array, max);
        System.out.println("Sorted Array: " + Arrays.toString(array));

    }

    /**
     * Counting Sort
     *  - Count the number of items in each array that have each value, then copy each value in order the required
     *  times back into the array.
     *
     *  - O(N) (N steps initializing and O steps counting values)
     *  - if N is relatively small compared to O, then it is much faster than O(N LOGN)
     *      - This means that performance depends on the RANGE OF VALUES
     */

    private static void sort(int[] values, int max) {

        // Set array to hold our counts
        int[] counts = new int[max + 1];

        // count items w/ each value.
        for (int i = 0; i < values.length; i++) {
            counts[values[i]]++;
        }

        System.out.println("\tCounts:");
        for (int i = 0; i <= max; i++) {
            if(counts[i] != 0) {
                System.out.println("\t" + i + " = " + counts[i]);
            }
        }

        // copy back
        int index = 0;
        for (int i = 0; i <= max; i++) {
            // copy value i into array counts[i] times
            for (int j = 0; j < counts[i]; j++) {
                values[index] = i;
                index++;
            }
        }
    }

    private static int[] populate(int max) {
        int[] array = new int[max];
        IntStream.rangeClosed(1, max).forEach(value -> array[value - 1] = ExecUtils.getRandom(max, 1));

        return array;
    }
}
