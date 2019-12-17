package Java.EssentialAlgorithms.Chapter9_Recursion.SelectionsAndPermutations;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.IntStream;

public class PermuteKofNWithoutDupes {



    public static void main(String[] args) {

        // Sizes
        int n = ExecUtils.getRandom(10, 1);
        int k = ExecUtils.getRandom(n, 1);

        // Storage
        int[] selections = new int[k];
        List<String> items = populate(n);
        List<List<String>> results = new ArrayList<>();

        System.out.println("Initial: " + items);
        System.out.println("K: " + k + "\nN: " + n);

        // Logic
        long start = System.nanoTime();
        permute(0, selections, items, results);
        long end = System.nanoTime();
        print(results);

        System.out.println("K: " + k + "\nN: " + n);
        System.out.println("Original: " + items);
        System.out.println("Time(ms): " + TimeUnit.NANOSECONDS.toMillis(end - start));

    }

    static void permute(int index, int[] selections, List<String> items, List<List<String>> results) {

        List<String> result = new ArrayList<>();
        if (index == selections.length) {
            for (Integer selection : selections)
                result.add(items.get(selection));
            results.add(result);
        } else {
            // Loop through each item.
            for (int i = 0; i < items.size(); i++) {
                boolean used = false;
                /*
                    loop up to (non-inclusive) index, and mark the index in use if it has been used.
                    This is the main difference to exclude dupes.
                */
                for (int j = 0; j < index; j++) {
                    if (selections[j] == i)
                        used = true;
                }

                /*
                    if 'i' is NOT in use, we are safe to use it and continue looking for
                    additional permutations.
                 */
                if (!used) {
                    selections[index] = i;
                    permute(index + 1, selections, items, results);
                }
            }
        }
    }

    static void print(List<List<String>> lists) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < lists.size(); i++) {
            sb.append(lists.get(i)).append("\t\t");

            if ((i + 1) % 8 == 0)
                sb.append('\n');
        }
        System.out.println(sb);
    }

    static List<String> populate(int max_size) {
        List<String> list = new ArrayList<>();
        IntStream.rangeClosed(1, max_size).forEach(
                value -> list.add(String.valueOf(ExecUtils.getRandom(max_size * 2, 1))));
        return list;
    }
}
