package Java.EssentialAlgorithms.Chapter9_Recursion.SelectionsAndPermutations;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class SelectKOfNWithDupes {

    public static void main(String[] args) {
        List<List<String>> results = new ArrayList<>();
        List<Integer> selections = new ArrayList<>();
        List<String> items = populate();
        System.out.println("Initial: " + items);

        select(0, selections, items, results);
        print(results);
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
    static void select(int index, List<Integer> selections, List<String> items, List<List<String>> results) {

        List<String> result = new ArrayList<>();
        if (index == selections.size()) {
            for (Integer selection : selections) {
                result.add(items.get(selection));
            }
            results.add(result);
        } else {
            int start;
            if (index > 0) {
                start = selections.get(index - 1);
                for (int i = start; i < items.size(); i++) {
                    selections.set(index, i);
                    select(index + 1, selections, items, results);
                }
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

    static List<String> populate() {
        List<String> list = new ArrayList<>();
        IntStream.rangeClosed(1, 10).forEach(
                value -> list.add(String.valueOf(ExecUtils.getRandom(15, 1))));
        return list;
    }

}
