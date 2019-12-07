package Java.EssentialAlgorithms.Chapter6_Sorting.ON2;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;
import java.util.stream.IntStream;

public class BubbleSortExec1 {
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
        boolean unsorted = true;
        int counter = 1;
        while (unsorted){

            /*
                Set unsorted to false. If we can iterate through the entire array w/o
                entering the if condition, then the array is sorted.
             */
            unsorted = false;

            System.out.println("===== Iteration #" + counter);

            for (int i = 1; i < array.length; i++) {

                if(array[i] < array[i - 1]) {
                    // Just Demo Print Statements.
                    System.out.println("\tPreSort: " + Arrays.toString(array));
                    System.out.println("\t\tSwapping: " + array[i] + "[" + i + "] With Best: "
                            + array[i - 1] + "[" + (i - 1) + "]");

                    int temp = array[i];
                    array[i] = array[i - 1];
                    array[i - 1] = temp;
                    unsorted = true;
                    System.out.println("\tPostSort: " + Arrays.toString(array) + "\n");
                }
            }
            counter++;
        }
    }
}
