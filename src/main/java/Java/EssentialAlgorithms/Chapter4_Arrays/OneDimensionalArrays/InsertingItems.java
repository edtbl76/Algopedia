package Java.EssentialAlgorithms.Chapter4_Arrays.OneDimensionalArrays;

import java.util.Arrays;

public class InsertingItems {

    public static void main(String[] args) {
        Integer[] integers = new Integer[0];

        /**
         * Closed loop iteration from 1 - 5 to seed my array.
         */
        for(int i = 1; i <= 5; i++) {
            integers = insertItem(integers, i, i - 1);
            System.out.println("Size: " + integers.length + " Content: " + Arrays.toString(integers));
        }
    }

    private static Integer[] insertItem(Integer[] array, Integer value, int position) {
        /**
         * Call to a resize function. Java doesn't support resizing arrays, so I have to perform a workaround
         * to demonstrate what is actually going on.
         */
        Integer[] copy = resizeArray(array, array.length + 1);
        for(int i = copy.length - 1;i >= position + 1;i--) {
            System.out.println(i + " " + position);
            copy[i] = array[i - 1];
        }
        copy[position] = value;

        return copy;
    }

    private static Integer[] resizeArray(Integer[] array, int new_length) {
        /**
         * We create a new array of the target length.
         * - make sure that we don't truncate the original structure by specifying a smaller value.
         * - then copy the data from one array to the other.
         */
        Integer[] new_array = new Integer[new_length];
        int preserveLength = Math.min(array.length, new_length);
        if (preserveLength > 0) {
            for (int i = 0; i < array.length; i++)
                new_array[i] = array[i];
        }

        return new_array;

    }
}
