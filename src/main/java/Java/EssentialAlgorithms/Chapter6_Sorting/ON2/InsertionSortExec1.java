package Java.EssentialAlgorithms.Chapter6_Sorting.ON2;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;
import java.util.stream.IntStream;

public class InsertionSortExec1 {

    public static void main(String[] args) {
        int[] array = new int[10];
        populate(array, 10);

        System.out.println("Unsorted : " + Arrays.toString(array));
        insertionSort(array);
        System.out.println("Sorted   : " + Arrays.toString(array));
    }

    private static void populate(int[] array, int max) {
        IntStream.rangeClosed(1, max).forEach(value -> {
            array[value - 1] = ExecUtils.getRandom(max, 1);
        });
    }

    /**
     * INSERTION SORT:
     *  - take an item from an list of input values and insert it into the proper position of a sorted output list
     *
     *  I call this Card Sorting 1:
     *  - Let's pretend I've been dealt a hand of 7 cards.
     *  - the first card to the left represents my sorted output list with 1 card.
     *  - the remaining 6 cards to the right represents my input list.
     *  - I will take cards from the input list (we'll say I take the first card to the left) and I compare that card
     *  to each card in the sorted output list starting at the beginning.
     *      - Once I find a card in the output list w/ a greater value than the card in my hand, I insert the card in my
     *      hand before the card with the greater value.
     *      - I repeat these steps until the input list is empty (and the output list is fully sorted).
     */
    private static void insertionSort(int[] array) {
        for (int i = 0; i < array.length; i++) {

            System.out.println("=====");
            /*
                find the first value[j] that is >= value[i]
                if this value is >= to the current value, then we don't need to sort it.
             */
            int j = 0;
            while (array[j] < array[i])
                j++;
            System.out.println("\tComparing : " + array[j] + " [" + j + "]");

            // set result to value[i]. This is the value we are interested in sorting.
            int result = array[i];
            System.out.println("\tSorting   : " + result + " [" + i + "]");

            /*
                if arr[j]  < arr[i], then
                we start at our current "i", and move everything down as long as "i" is > j.
                This moves everything down so that we can insert at j in the following step.
             */
            for (int k = i; k > j; k--) {
                System.out.println("\t\tMoving: " + array[k - 1] + " [" + k + "->" + (k - 1) + "]");
                array[k] = array[k - 1];
            }
            System.out.println("\tPostMove: " + Arrays.toString(array));
            /*
                now that we have moved everything down, insert at the "empty" location
                - if array[i] = array[j], we are just writing the same value to the same cell.
             */
            array[j] = result;
            System.out.println("\t\tWriting: " + result + " to [" + j + "]");
            System.out.println("\tPostWrite: " + Arrays.toString(array));
        }

    }
}
