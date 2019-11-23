package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.LinkedListSentinelImpl;

public class LLImplExec4 {
    public static void main(String[] args) {
        /*
            This demonstrates a default constructor that creates a sentinel.
            - However, to use the data structure effectively, we are demonstrating that the
            sentinel is not counted as an element of the structure. It's just plumbing.
         */
        LinkedListSentinelImpl<Integer> list = new LinkedListSentinelImpl<>();
        if(list.isEmpty())
            System.out.println("We don't count the sentinel!");

        System.out.println("Anybody There?: [" + list + "]");
        System.out.println("Size: " + list.size());
    }


}
