package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.DoublyLinkedListImpl;

import java.util.Arrays;

public class DLLImplExec4 {

    public static void main(String[] args) {
        DoublyLinkedListImpl<Integer> list = new DoublyLinkedListImpl<>(Arrays.asList(1,2,3,4,5));
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        DoublyLinkedListImpl<Integer> newList = list.copy();
        System.out.println("Size: " + newList.size() + " Content: [" + newList + "]");

    }
}
