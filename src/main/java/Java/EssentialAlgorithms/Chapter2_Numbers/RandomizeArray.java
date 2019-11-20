package Java.EssentialAlgorithms.Chapter2_Numbers;

import java.util.Arrays;
import java.util.List;

public class RandomizeArray {

    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5);
        list.forEach(integer -> System.out.print(integer + " "));
        System.out.println();

        randomize(list);
        list.forEach(integer -> System.out.print(integer + " "));
        System.out.println();

    }

    private static void randomize(List<Integer> list) {
        for(int i = 0; i < list.size(); i++) {
            int new_index = (int) (Math.random() * list.size());
            int temp = list.get(i);
            list.set(i, list.get(new_index));
            list.set(new_index, temp);
        }
    }
}
