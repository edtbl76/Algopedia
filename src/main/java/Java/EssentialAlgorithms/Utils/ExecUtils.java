package Java.EssentialAlgorithms.Utils;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ExecUtils {

    /**
     * Populates an array with random ints based on a given array size.
     */
    public static int[] populate(int max) {
        int[] array = new int[max];
        IntStream.rangeClosed(1, max).forEach(value -> array[value - 1] = ExecUtils.getRandom(max, 1));
        return array;
    }

    public static List<Integer> populateCollection(int max, int size) {
        int[] array = new int[size];
        IntStream.rangeClosed(1, size).forEach(value -> array[value - 1] = ExecUtils.getRandom(max, 1));
        return Arrays.stream(array).boxed().collect(Collectors.toList());
    }

    public static List<Integer> populateCollection(int max, int size, boolean sorted) {
        int[] array = new int[size];
        IntStream.rangeClosed(1, size).forEach(value -> array[value - 1] = ExecUtils.getRandom(max, 1));
        List<Integer> results = Arrays.stream(array).boxed().collect(Collectors.toList());

        if (sorted)
            Collections.sort(results);

        return results;
    }

    /**
     * Gets a random number, within a given range.
     */
    public static int getRandom(int max, int min) {
        return (int)(Math.random() * ((max - min) + 1) + min);
    }


    /**
     * Takes an int and prints the result if greater than -1
     */
    public static void findIndexPrinter(int target, int result) {

        if (result > 0) {
            System.out.println("Found " + target + " at " + result + "!");
        } else {
            System.out.println("No " + target + "s here :(");
        }
    }


}


