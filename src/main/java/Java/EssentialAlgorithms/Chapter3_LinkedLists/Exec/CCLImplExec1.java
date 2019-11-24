package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.CircularLinkedListImpl;

public class CCLImplExec1 {

    public static void main(String[] args) {
        CircularLinkedListImpl<Integer> list = new CircularLinkedListImpl<>();
        assert list.isEmpty();
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // add append
        list.add(1);
        list.add(2);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        list.add(1, 3);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        list.add(0, 4);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        list.add(list.size(), 5);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        list.addFirst(6);
        list.addLast(7);
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

    }
}
