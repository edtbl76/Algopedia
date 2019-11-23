package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.DoublyLinkedListImpl;

import java.util.Arrays;

public class DLLImplExec2 {
    public static void main(String[] args) {
        DoublyLinkedListImpl<Integer> list = new DoublyLinkedListImpl<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10));
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // DeleteAtHead
        list.deleteAtHead();
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // DeleteAtTail
        list.deleteAtTail();
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // delete() middle
        list.delete(4);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // delete() head
        list.delete(2);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // delete() tail
        list.delete(9);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // clear
        list.clear();
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // Sorting Inserts
        list.insertSorted(5);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");
        list.insertSorted(1);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");
        list.insertSorted(7);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");
        list.insertSorted(2);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");
        list.insertSorted(9);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");
        list.insertSorted(8);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

    }
}
