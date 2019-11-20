package Java.DataStructures.Lists.Exec;

import Java.DataStructures.Lists.CircularLinkedList;

public class CircularLinkedListExample {
    public static void main(String[] args) {
        CircularLinkedList<Integer> cll = new CircularLinkedList<>();
        assert cll.isEmpty();

        cll.insert(5);
        System.out.println(cll);

        cll.append(10);
        System.out.println(cll);

        cll.delete();
        System.out.println(cll);

        cll.insert(20);
        cll.insert(30);
        System.out.println(cll);

        for (int i = 1; i <= cll.size(); i++) {
            System.out.println("Position" + i + ": " + cll.get(i));
        }

        cll.clear();
        assert cll.isEmpty();
        System.out.println(cll);
    }
}
