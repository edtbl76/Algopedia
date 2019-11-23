package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.LinkedListSentinelImpl;

import java.util.Arrays;

public class LLImplExec8 {
    public static void main(String[] args) {
        LinkedListSentinelImpl<Integer> list = new LinkedListSentinelImpl<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        list.insert(4, 10);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        list.insert(2, 20);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

    }
}
