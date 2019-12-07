package Java.EssentialAlgorithms.Chapter7_Searching;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;

public class InterpolationSearch {

    public static void main(String[] args) {
        int[] array = ExecUtils.populate(9);
        System.out.println("Initial " + Arrays.toString(array));
        Arrays.parallelSort(array);
        System.out.println("Sorted: " + Arrays.toString(array));

        int target = ExecUtils.getRandom(1, 10);
        int index = findIndex(array, target, 0);
        if (index == -1)
            System.out.println("No " + target + "s here!");
        else
            System.out.println("Found " + target + " at : " + index);

    }

    /**
     * Interpolation Search
     * - uses value of target item to guess where in the array it might lie to achieve much faster times.
     *
     * TIME: O(N) to O(Log(Log N)
     */
    private static int findIndex(int[] values, int target, int steps) {
        int min = 0;
        int max = values.length - 1;
        while (min <= max) {
            steps++;
            System.out.println("\tBounds: (" + min + "," + max + ") Steps: " + steps);

            // no divide by zero!
            if (values[min] == values[max]) {
                if (values[min] == target)
                    return min;
                return -1;
            }

            // find the divider
            int mid = min + (max - min) * (target - values[min]) / (values[max] - values[min]);
            System.out.println("\t\tMid: " + mid);

            // if mid is ridiculous, bail out
            if ((mid < min) || (mid > max))
                return -1;

            // evaluate what half we search
            if (values[mid] < target)
                min = mid + 1;
            else if (values[mid] > target)
                max = mid - 1;
            else
                return mid;
        }
        return -1;
    }
}
