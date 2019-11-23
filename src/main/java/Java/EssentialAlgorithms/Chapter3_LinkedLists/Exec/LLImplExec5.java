package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.LinkedListSentinelImpl;

import java.util.stream.IntStream;

public class LLImplExec5 {
    public static void main(String[] args) {
        /*
            Before we continue we need to handle insertion and size management
            1.) showing the old constructor
            2.) showing a new constructor that will initialize a single value of E
            3.) Seed it up w/ a range that calls our insert() method.
         */
        LinkedListSentinelImpl<Integer> list_blank = new LinkedListSentinelImpl<>();
        assert list_blank.isEmpty();

        LinkedListSentinelImpl<Integer> list = new LinkedListSentinelImpl<>(1);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // seed it up and then print what we have.
        IntStream.rangeClosed(2, 5).forEach(list::insertAtHead);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");



    }
}
