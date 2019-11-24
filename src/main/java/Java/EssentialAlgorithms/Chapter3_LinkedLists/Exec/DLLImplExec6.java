package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.DoublyLinkedListImpl;

import java.util.Arrays;

public class DLLImplExec6 {
    public static void main(String[] args) {
        DoublyLinkedListImpl<Integer> list = new DoublyLinkedListImpl<>(Arrays.asList(
                101, 3, 85, 62, 4, 9765, 22, 18, 4, 2, 26, 44, 8));
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        DoublyLinkedListImpl<Integer> sorted = list.selectionSort();
        System.out.println("Size: " + sorted.size() + " Content: [" + sorted + "]");

    }
}
