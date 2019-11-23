package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.LinkedListSentinelImpl;

import java.util.Arrays;

public class LLImplExec9 {
    public static void main(String[] args) {
        LinkedListSentinelImpl<Integer> list = new LinkedListSentinelImpl<>(Arrays.asList(1, 2, 3, 4, 5));


        // HIT
        System.out.println(list.findCell(3));

        // MISS
        System.out.println(list.findCell(47));

        // insertAfter
        list.insertAfter(4, 7);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // This is actually inserting at Tail, but its handed off,.
        list.insertAfter(5, 8);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // Inserting after nonexistent (this ignores the input)... we could throw IndexOutOfBounds.
        list.insertAfter(50, 50);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // This is actually inserting before Head.
        list.insertBefore(1, 9);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // This is an insert in the middle
        list.insert(3, 10);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

    }
}
