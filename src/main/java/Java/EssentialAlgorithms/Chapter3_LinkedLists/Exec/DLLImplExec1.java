package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.DoublyLinkedListImpl;

public class DLLImplExec1 {
    public static void main(String[] args) {
        DoublyLinkedListImpl<Integer> list = new DoublyLinkedListImpl<>();
        assert list.isEmpty();
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // Insert at Head
        list.insertAtHead(1);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");
        list.insertAtHead(2);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // tail insertion
        list.insertAtTail(3);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");
        list.insertAtTail(4);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // insert after
        list.insertAfter(1, 5);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // insert after(tail)
        list.insertAfter(4, 6);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // insert before
        list.insertBefore(5, 7);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // insert before head
        list.insertBefore(2, 8);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

    }
}
