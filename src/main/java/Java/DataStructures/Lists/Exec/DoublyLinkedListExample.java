package Java.DataStructures.Lists.Exec;

import Java.DataStructures.Lists.DoublyLinkedList;

public class DoublyLinkedListExample {
    public static void main(String[] args) {
        DoublyLinkedList dll = new DoublyLinkedList();
        assert dll.isEmpty();

        dll.insertHead(13);
        dll.insertHead(7);
        dll.insertHead(10);
        System.out.println(dll);

        dll.insertTail(11);
        System.out.println(dll);

        dll.deleteTail();
        System.out.println(dll);

        dll.delete(7);
        System.out.println(dll);

        dll.insertOrdered(23);
        dll.insertOrdered(67);
        dll.insertOrdered(3);
        System.out.println(dll);

        dll.clear();
        assert dll.isEmpty();
    }
}
