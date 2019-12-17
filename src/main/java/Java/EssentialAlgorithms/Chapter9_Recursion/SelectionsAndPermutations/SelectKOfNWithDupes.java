package Java.EssentialAlgorithms.Chapter9_Recursion.SelectionsAndPermutations;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class SelectKOfNWithDupes {

    public static void main(String[] args) {

        //int k = ExecUtils.getRandom(10, 1);
        //int n = ExecUtils.getRandom(10, 1);
        int k = 10;
        int n = 29;

        List<List<String>> results = new ArrayList<>();
        List<String> items = populate(n);

        int[] selections = new int[k];

        System.out.println("Initial: " + items);
        System.out.println("k: " + k + " n: " + n);

        select(0, selections, items, results);
        print(results);
        System.out.println("K: " + k + "\nN: " + n + "\nTotal: " + results.size());
    }

    /**
     *
     * @param index         gives the index of the item in the selection that the this recursive call
     *                      to the algo should set.
     * @param selections    array to hold indices of items
     *                      EX: if selections has 2 entries of 8 and 9, the selection includes the
     *                      items w/ indices 8 and 9
     * @param items         array of items from which selections should be made
     * @param results       list of list of items representing the complete selections.
     */
    static void select(int index, int[] selections, List<String> items, List<List<String>> results) {

        List<String> result = new ArrayList<>();
        if (index == selections.length) {
            for (Integer selection : selections) {
                result.add(items.get(selection));
            }
            results.add(result);
        } else {
            int start = 0;
            if (index > 0) {
                start = selections[index - 1];
            }
            for (int i = start; i < items.size(); i++) {
                selections[index] = i;
                select(index + 1, selections, items, results);
            }

        }
    }

    static void print(List<List<String>> lists) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < lists.size(); i++) {
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
