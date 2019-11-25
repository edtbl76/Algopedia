package Java.EssentialAlgorithms.Chapter4_Arrays.OneDimensionalArrays;

import java.util.Arrays;

public class MinMaxAverage {

    public static void main(String[] args) {

        // Create and store an array
        Integer[] integers = new Integer[]{25, 16, 11, 100, 69};
        System.out.println(Arrays.toString(integers));
        System.out.println("Minimum = " + min(integers));
        System.out.println("Maximum = " + max(integers));
        System.out.println("Average = " + average(integers));

    }

    private static Integer min(Integer[] array) {
        Integer min_value = array[0];

        /*
            Array can start at 1, because we've already collected the value at 0.
            - array.lenght is not inclusive in the conditional, because we are using a zero-based index.
         */
        for(int i = 1; i < array.length; i++) {
            if(array[i] < min_value)
                min_value = array[i];
        }
        return min_value;
    }

    private static Integer max(Integer[] array) {
        Integer max_value = array[0];

        for (int i = 1; i < array.length; i++) {
            if (array[i] > max_value)
                max_value = array[i];
        }
        return max_value;
    }

    private static Double average(Integer[] array) {
        Integer total = 0;
        for (Integer integer : array)
            total += integer;

        return (double) total / array.length;
    }
}
