package Java.EssentialAlgorithms.Chapter9_Recursion.SelectionsAndPermutations;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.stream.IntStream;

public class SelectKOfNWithoutDupes {

    public static void main(String[] args) {

        //int k = ExecUtils.getRandom(10, 1);
        //int n = ExecUtils.getRandom(10, 1);

        int k = 10;
        int n = 29;
        List<List<String>> results = new ArrayList<>();
        List<String> items = populate(n);


        int[] selections = new int[k];
        System.out.println("Initial: " + items);

        // first select
        long start = System.nanoTime();
        select(0, selections, items, results);
        long end = System.nanoTime();

        // print it out
        print(results);
        System.out.println("K: " + k);
        System.out.println("N: " + n);
        System.out.println("TotalResults: " + results.size());
        System.out.println("Elapsed Time: " + TimeUnit.NANOSECONDS.toMillis(end - start));

    }

    private static void select(int index, int[] selections, List<String> items, List<List<String>> results) {

        List<String> result = new ArrayList<>();
        if (index == selections.length) {
            for (Integer selection : selections)
                result.add(items.get(selection));
            results.add(result);
        } else {
            int start = 0;
            /*
                NOTE: Here is the without duplicates trick.
                Remember. if start == target, then we will evaluate matches of our target in our final solution.
                However, if we set start to be "+ 1", we won't evaluate matches.
             */
            if (index > 0)
                start = selections[index - 1] + 1;
            for (int i = start; i < items.size(); i++) {
                selections[index] = i;
                select(index + 1, selections, items, results);
            }
        }
    }

    private static void print(List<List<String>> lists) {
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
