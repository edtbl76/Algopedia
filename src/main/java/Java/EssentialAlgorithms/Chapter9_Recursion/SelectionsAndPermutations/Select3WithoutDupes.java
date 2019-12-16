package Java.EssentialAlgorithms.Chapter9_Recursion.SelectionsAndPermutations;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Select3WithoutDupes {

    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        populate(list);
        System.out.println("Initial: " + list);

        List<List<String>> selected = selection(list);
        print(selected);
        System.out.println("Permutations: " + selected.size());

    }

    static List<List<String>> selection(List<String> items) {
        List<List<String>> result = new ArrayList<>();
        for (int i = 0; i < items.size(); i++) {
            for (int j = i + 1; j < items.size(); j++) {
                for (int k = j + 1; k < items.size(); k++) {
                    result.add(Arrays.asList(
                            items.get(i), items.get(j), items.get(k)
                    ));
                }
            }
        }
        return result;
    }

    static void populate(List<String> list) {
        for(int i = 0; i < 10; i++) {
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
