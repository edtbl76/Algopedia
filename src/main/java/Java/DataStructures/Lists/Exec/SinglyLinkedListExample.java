package Java.DataStructures.Lists.Exec;

import Java.DataStructures.Lists.SinglyLinkedList;

public class SinglyLinkedListExample {

    public static void main(String[] args) {
        SinglyLinkedList list = new SinglyLinkedList();
        assert list.isEmpty();
        assert list.toString().equals("");

        list.insertHead(5);
        list.insertHead(7);
        list.insertHead(10);
        assert list.toString().equals("10->7->5");
        System.out.println(list);

        list.deleteHead();
        assert list.toString().equals("7->5");
        System.out.println(list);

        list.insertAt(11, 2);
        assert list.toString().equals("7->5->11");
        System.out.println(list);

        list.deleteAt(1);
        assert list.toString().equals("7->11");
        System.out.println(list);

        list.clear();
        assert list.isEmpty();
        System.out.println(list);

        SinglyLinkedList list1 = new SinglyLinkedList();
        SinglyLinkedList list2 = new SinglyLinkedList();

        for (int i = 10; i >= 2; i -= 2) {
            list1.insertSorted(i);
            list2.insertSorted(i - 1);
        }

        assert list1.toString().equals("2->4->6->8->10");
        assert list2.toString().equals("1->3->5->7->9");
        assert SinglyLinkedList.merge(list1, list2).toString().equals("1->2->3->4->5->6->7->8->9->10");
        System.out.println(list1);
        System.out.println(list2);
        System.out.println(SinglyLinkedList.merge(list1, list2));


    }
}
