package Java.EssentialAlgorithms.Chapter9_Recursion.SelectionsAndPermutations;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Select3WithDupes {

    public static void main(String[] args) {
        List<String> items = new ArrayList<>();
        populate(items);
        System.out.println("Initial List: " + items);

        List<List<String>> result = selection(items);
        print(result);
        System.out.println("Permutations: " + result.size());

    }

    static List<List<String>> selection(List<String> list) {
        List<List<String>> results = new ArrayList<>();
        for (int i = 0; i < list.size(); i++) {
            for (int j = i; j < list.size(); j++) {
                for (int k = j; k < list.size(); k++) {
                    results.add(Arrays.asList(list.get(i), list.get(j), list.get(k)));
                }
            }
        }
        return results;
    }

    static void populate(List<String> list) {
        for(int i = 0; i < 5; i++) {
            String str = String.valueOf(ExecUtils.getRandom(15, 1));
            list.add(str);
        }
    }

    static void print(List<List<String>> list) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < list.size(); i++) {
            sb.append(list.get(i)).append("\t\t");

            if ((i + 1) % 8 == 0)
                sb.append("\n");
        }
        System.out.println(sb);
    }
}
