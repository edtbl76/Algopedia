package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.Cell;
import Java.EssentialAlgorithms.Chapter3_LinkedLists.LinkedListSentinelImpl;

import java.util.Arrays;
import java.util.stream.IntStream;

public class LLImplExec6 {

    public static void main(String[] args) {
        /*
            Added a new constructor so that I can make insertion easier (this actually uses insertAtTail)
         */
        LinkedListSentinelImpl<Integer> list = new LinkedListSentinelImpl<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        /*
            Now we revisit the problem from LLImplExec3. Using a sentinel we can see that we are able to access
            the sentinel as the value BEFORE our first structural element.
                - this can be very useful in circular structures, because it creates a consistent insertion point.
         */
        IntStream.rangeClosed(1, 5).forEach(
                value -> {
                    System.out.println("Value: " + value + " Before: " + list.findCellBefore(value));
                }
        );
    }
}
