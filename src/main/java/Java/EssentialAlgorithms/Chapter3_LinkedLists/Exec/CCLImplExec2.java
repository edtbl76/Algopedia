package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.CircularLinkedListImpl;

import java.util.Arrays;
import java.util.stream.IntStream;

public class CCLImplExec2 {
    public static void main(String[] args) {
        CircularLinkedListImpl<Integer> list = new CircularLinkedListImpl<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        System.out.println("Is there a 5? " + list.contains(5));
        System.out.println("Heads: " + list.getFirst());
        System.out.println("Tails: " + list.getLast());

        IntStream.rangeClosed(0, 4).forEach(
                value -> {
                    System.out.println(list.indexOf(value + 1) + ": " + list.get(value));
                    System.out.println("Removing: " + list.remove(value));
                    list.add(value, value + 1);
                    System.out.println("Adding: " + (value + 1) + "@[" + value + "]");

                }
        );
        System.out.println();

        System.out.println("Size: " + list.size() + " Content: [" + list + "]");




    }
}
