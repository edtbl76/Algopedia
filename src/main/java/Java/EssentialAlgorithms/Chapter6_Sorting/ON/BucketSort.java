package Java.EssentialAlgorithms.Chapter6_Sorting.ON;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.IntStream;

public class BucketSort {

    public static void main(String[] args) {
        int[] array = populate(20);
        System.out.println("Initial Array: " + Arrays.toString(array));
        sort(array, 5);
        System.out.println("Sorted Array: " + Arrays.toString(array));

    }

    /**
     *  BUCKET SORT (aka BIN SORT)
     *      - (DISTRIBUTE)  divides item into buckets.
     *      - (SORT)  sorts items by using an algorithm on each bucket (or by calling bucket sort)
     *      - (GATHER) concatenates buckets back into original array
     *
     *      Array w/ N  items and M buckets means that each bucket has roughly N/M items
     *      - M must be a fairly large fraction of N  to perform well.
     */
    private static void sort(int[] values, int count) {
        List<List<Integer>> buckets = new ArrayList<>(count);

        // PreSeed the buckets
        for (int i = 0; i < count; i++) {
            buckets.add(i, new ArrayList<>());
        }

        // Assign Numbers to Buckets.
        for (int value : values) {
            buckets.get(simpleHash(value, count)).add(value);
        }

        System.out.println("\tBuckets (PreSort)  : ");
        buckets.forEach(integers -> System.out.println("\t" + integers));

        buckets.forEach(Collections::sort);

        System.out.println("\tBuckets (PostSort) : ");
        buckets.forEach(integers -> System.out.println("\t" + integers));

        // Merge Buckets
        AtomicInteger i = new AtomicInteger();
        buckets.forEach(integers -> {
            integers.forEach(integer -> {
                values[i.getAndIncrement()] = integer;
            });
        });

    }

    private static int[] populate(int max) {
        int[] array = new int[max];
        IntStream.rangeClosed(1, max).forEach(value -> array[value - 1] = ExecUtils.getRandom(max, 1));

        return array;
    }


    private static int simpleHash(int num, int count) {
        return num / count;
    }

}
