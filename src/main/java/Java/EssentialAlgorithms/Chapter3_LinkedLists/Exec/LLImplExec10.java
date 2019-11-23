package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.LinkedListSentinelImpl;

import java.util.Arrays;

public class LLImplExec10 {
    public static void main(String[] args) {
        LinkedListSentinelImpl<Integer> list = new LinkedListSentinelImpl<>(Arrays.asList(1,2,3,4,5,6,7,8,9));
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // Head Delete
        list.deleteAtHead();
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // Tail Delete
        list.deleteAtTail();
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // Delete After (somewhere in the middle)
        list.deleteAfter(4);;
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // Delete After (tail)
        list.deleteAfter(7);;
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // Delete After (non existent)
        list.deleteAfter(9);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // delete at position
        list.delete(2);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        list.delete(0);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        list.delete(list.size());
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        list.delete(100);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        list.clear();
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

    }
}
