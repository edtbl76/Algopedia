package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.LinkedListSentinelImpl;

import java.util.stream.IntStream;

public class LLImplExec7 {
    public static void main(String[] args) {
        LinkedListSentinelImpl<Integer> list = new LinkedListSentinelImpl<>();
        IntStream.rangeClosed(1, 20).forEach(value -> {
            if (value % 2 == 0) {
                list.insertAtHead(value);
            } else {
                list.insertAtTail(value);
            }
        });
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");
    }
}
