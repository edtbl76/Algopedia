package Java.EssentialAlgorithms.Chapter7_Searching;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;

public class LinearSearch {

    public static void main(String[] args) {
        int[] array = ExecUtils.populate(10);
        System.out.println("Array: " + Arrays.toString(array));

        int index = findIndex(array, 5);
        if (index != -1)
            System.out.println("Found a five at " + index);
        else
            System.out.println("No fives here!");
    }

    /**
     * Linear Search is pretty obvious. Exhaustively Keep looking for the specific value, unless it is impossible to
     * find it.
     *
     * PRO
     * - works on linked lists and unsorted lists
     * CON
     * - SLOWER than binary search
     *
     * TIME: O(N)
     */
    private static int findIndex(int[] values, int target) {
        for(int i = 0; i < values.length; i++) {
            if(values[i] == target)
                return i;

            // If the value at i is greater than the target, we can stop searching, because it ain't there.
            if(values[i] > target)
                return -1;
        }
        return -1;
    }
}
