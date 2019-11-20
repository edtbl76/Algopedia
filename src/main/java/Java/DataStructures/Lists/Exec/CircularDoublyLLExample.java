package Java.DataStructures.Lists.Exec;

import Java.DataStructures.Lists.CircularDoublyLinkedList;

public class CircularDoublyLLExample {
    public static void main(String[] args) {
        CircularDoublyLinkedList<Integer> cdll = new CircularDoublyLinkedList<>();
        assert cdll.isEmpty();

        cdll.insertAtHead(5);       // 5
        cdll.insertAtTail(10);      // 5 -> 10
        cdll.insertAtTail(11);      // 5 -> 10 -> 11
        cdll.insertAtHead(77);      // 77 -> 5 -> 10 -> 11
        cdll.insertAtTail(105);     // 77 -> 5 -> 10 -> 11 -> 105

        System.out.println("Head: " + cdll.getHead());
        System.out.println("Tail: " + cdll.getTail());
        System.out.println(cdll);
        System.out.println(cdll.reversed());


        System.out.println("Forward");
        for (int i = 1; i <= cdll.size(); i++) {
            System.out.println("Position" + i + ": " + cdll.get(i));
        }
        System.out.println("\nBackward");
        for (int i = 1; i <= cdll.size(); i++) {
            System.out.println("Position" + i + ": " + cdll.get(i, true));
        }

        cdll.deleteHead();
        cdll.deleteTail();
        System.out.println("Head: " + cdll.getHead());
        System.out.println("Tail: " + cdll.getTail());
        System.out.println(cdll);
        System.out.println(cdll.reversed());

        cdll.clear();
        assert cdll.isEmpty();
        System.out.println(cdll);


    }
}
