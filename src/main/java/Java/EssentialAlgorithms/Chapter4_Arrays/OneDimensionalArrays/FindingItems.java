package Java.EssentialAlgorithms.Chapter4_Arrays.OneDimensionalArrays;

import java.util.Arrays;

public class FindingItems {

    public static void main(String[] args) {

        // Create and store an array
        Integer[] integers = new Integer[]{1, 2, 3, 4, 5};
        System.out.println(Arrays.toString(integers));

        // Get Indexes
        for (Integer integer : integers) {
            System.out.println(integer + " is at index: [" + indexOf(integers, integer)+ "]");
        }

    }

    private static Integer indexOf(Integer[] array, Integer target) {
        for(int i = 0; i < array.length; i++) {
            if(array[i] == target)
                return i;
        }
        return -1;
    }


}
