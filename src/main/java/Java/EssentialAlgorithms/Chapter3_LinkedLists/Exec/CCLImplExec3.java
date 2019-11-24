package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.CircularLinkedListImpl;

import java.util.Arrays;

public class CCLImplExec3 {
    public static void main(String[] args) {
        CircularLinkedListImpl<Integer> list = new CircularLinkedListImpl<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        System.out.println("Loopy? " + list.isLoop());
        System.out.println("TracedLoop? " + list.hasLoopRetracing());

    }

}
