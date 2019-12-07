package Java.EssentialAlgorithms.Chapter7_Searching;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;

public class BinarySearch {

    public static void main(String[] args) {
        int[] array = ExecUtils.populate(10);
        System.out.println("Initial " + Arrays.toString(array));
        Arrays.parallelSort(array);
        System.out.println("Sorted: " + Arrays.toString(array));

        int target = ExecUtils.getRandom(1, 10);
        int index = findIndex(array, target);
        if (index == -1)
            System.out.println("No fives here!");
        else
            System.out.println("Found " + target + "  at : " + index);
    }

    /**
     *  BINARY SEARCH
     *      - tracks largest & smallest indices that the target might have in the array.
     *          - starts at (0, length)
 *          - calculates middle index.
     *          - if target is < value at index, it resets max to search left half of array
     *          - else searches right half.
     *          - if = mid, returns.
     *
     *  TIME: O (LOG N)
     */

    private static int findIndex(int[] values, int target) {
        int min = 0;
        int max = values.length - 1;

        while (min <= max) {
            int mid = (min + max) / 2;
            System.out.println("\tBounds: (" + min + "," + max + ") Mid: " + mid);
            if (target < values[mid])
                max = mid - 1;
            else if(target > values[mid])
                min = mid + 1;
            else
                return mid;
        }
        return -1;
    }
}
