package Java.EssentialAlgorithms.Chapter6_Sorting.ONLOGN;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;
import java.util.stream.IntStream;

public class MergeSortExec1 {

    public static void main(String[] args) {
        int[] array = populate(8);
        System.out.println("Initial Array: " + Arrays.toString(array));
        sort(array);
        System.out.println("Sorted Array: " + Arrays.toString(array));


    }

    /**
     *  MergeSort:
     *  - Similar to QuickSort, but you'll note that the recursion happens before all of the business logic.
     *  (so we can merge the results after <-- this is a mneumonic device to help you remember the algorithm)
     *
     *  QuickSort creates two halves relative of the divider. MergeSort just cuts the array in half recursively.
     *  Once we've got a bunch of single valued arrays, we start zippering them back together.
     *  merging left and right into a scratch array.
     *
     *
     *  MergeSort can be PARALLELIZED, by sending each recursion to a new thread. However, since MergeSort's "halves"
     *  are contextual, a thread must wait until all of its subsequent calls are complete in order to "zip back up" to
     *  the final solution.
     *
     *  USE CASE:
     *  - merge sort is useful when all of the data sorted won't fit in memory at once.
     *
     */
    private static void sort(int[] values) {
        int[] temp = new int[values.length];
        mergeSort(values, temp, 0, values.length - 1, 1);

    }

    private static void mergeSort(int[] values, int [] scratch, int start, int end, int counter) {

        // make sure we have something to sort!
        if(start >= end) {
            System.out.println("\tSort Complete: " + Arrays.toString(values) + " (" + start + "," + end + ")");
            return;
        }
        System.out.print("\tSorting: " + Arrays.toString(values) + " (" + start + "," + end + ")");

        // create halves
        int midpoint = (start + end) / 2;
        System.out.println(" Around: " + midpoint);


        System.out.println("Iteration: === " + counter + " ===");
        counter++;

        // Sort the halves
        mergeSort(values, scratch, start, midpoint, counter);
        mergeSort(values, scratch, midpoint + 1, end, counter);
        /*
            I call this the ZIPPER.
            This is the merge part, where we merge the two halves together.
            - we compare the values sorted from the left to the right and store the lesser of the two in the scratch
         */

        int left = start;
        int right = midpoint + 1;
        int temp = left;
        while ((left <= midpoint) && (right <= end)) {
            if (values[left] <= values[right]) {
                scratch[temp] = values[left];
                System.out.println("\t\tScratchLeft : " + Arrays.toString(scratch));
                left++;
            } else {
                scratch[temp] = values[right];
                System.out.println("\t\tScratchRight: " + Arrays.toString(scratch));
                right++;
            }
            temp++;
        }

        /*
            Copy the leftovers
         */
        for (int i = left; i <= midpoint; i++) {
            scratch[temp] = values[i];
            System.out.println("\t\tLeftOvers :" + Arrays.toString(scratch));
            temp++;
        }
        for (int i = right; i <= end; i++) {
            scratch[temp] = values[i];
            System.out.println("\t\tRightOvers :" + Arrays.toString(scratch));
            temp++;
        }

        // copy values back into the original array
        for (int i = start; i <= end; i++) {
            values[i] = scratch[i];
        }
    }

    private static int[] populate(int max) {
        int[] array = new int[max];
        IntStream.rangeClosed(1, max).forEach(value -> array[value - 1] = ExecUtils.getRandom(max, 1));

        return array;
    }
}
