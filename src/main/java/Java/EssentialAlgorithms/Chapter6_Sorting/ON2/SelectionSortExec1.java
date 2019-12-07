package Java.EssentialAlgorithms.Chapter6_Sorting.ON2;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;
import java.util.stream.IntStream;

public class SelectionSortExec1 {

    public static void main(String[] args) {
        int[] array = new int[10];
        populate(array, 10);

        System.out.println("Unsorted : " + Arrays.toString(array));
        selectionSort(array);
    }

    private static void populate(int[] array, int max) {
        IntStream.rangeClosed(1, max).forEach(value -> {
            array[value - 1] = ExecUtils.getRandom(max, 1);
        });
    }

    /**
     * SELECTION SORT:
     * - this is the "opposite" of Insertion sort. I search an input list for the largest item and then add that value
     *   to the end of a growing sorted list.
     *
     * You guessed it... I call this Card Sorting 2:
     * Let's say I was dealt a hand of 7 cards.
     * - starting from the left most card, I'm going to look for the card with the greatest value.
     *  - once I have the largest card, I'm going to place that card to the right of the rest of the cards
     *      - We'll call this the beginning of our sorted output list.
     *  - repeat this process of searching for the largest card in the "input list" and appending it to the sorted
     *  output list.
     */
    private static void selectionSort(int[] array) {
        for (int i = 0; i < array.length; i++) {

            System.out.println("=====");

            /*
                Find smallest item that hasn't been sorted yet.
             */
            int smallestIndex = i;
            int smallestValue = array[i];

            /*
                compare the rest of the array against the "current best"
             */
            for (int j = i + 1; j < array.length; j++) {
                if (array[j] < smallestValue) {
                    smallestIndex = j;
                    smallestValue = array[j];
                }
            }

            System.out.println("\tPreSort : " + Arrays.toString(array));
            System.out.println("\t\tSwap: " + array[i] + "[" + i + "] with Best: "
                    + array[smallestIndex] + "[" + smallestIndex + "]");
            /*
                At this point we have the "best", so we just need to swap it into place
             */
            int temp = array[smallestIndex];    // store value at best index in temp variable
            array[smallestIndex] = array[i];    // set value at best index to our current value
            array[i] = temp;                    // swap in best value at the index of our current value.

            System.out.println("\tPostSort: " + Arrays.toString(array));
        }
    }
}
