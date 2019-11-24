package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.DoublyLinkedListImpl;

public class DLLImplExec3 {
    public static void main(String[] args) {
        DoublyLinkedListImpl<Integer> list = new DoublyLinkedListImpl<>();
        assert list.isEmpty();

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
        list.clear();
        assert list.isEmpty();
    }
}
