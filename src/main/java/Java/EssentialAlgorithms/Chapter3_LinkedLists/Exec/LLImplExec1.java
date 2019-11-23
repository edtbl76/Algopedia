package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.Cell;
import Java.EssentialAlgorithms.Chapter3_LinkedLists.LinkedListImpl;

public class LLImplExec1 {

    public static void main(String[] args) {
        Cell<Integer> cell1 = new Cell<>(5);
        Cell<Integer> cell2 = new Cell<>();
        cell2.setData(10);

        cell1.setNext(cell2);

        LinkedListImpl.iterate(cell1);

    }
}
