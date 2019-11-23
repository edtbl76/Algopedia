package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.Cell;
import Java.EssentialAlgorithms.Chapter3_LinkedLists.LinkedListImpl;

public class LLImplExec3 {

    public static void main(String[] args) {
        /*
            Set up a Linked List by initializing 2 cells, and wiring them together
         */
        Cell<Double> cell1 = new Cell<>(2.0);
        Cell<Double> cell2 = new Cell<>();
        cell2.setData(4.5);
        cell1.setNext(cell2);


        Cell<Double> result = LinkedListImpl.findCellBefore(cell1, 4.5);

        // This output shows how getData() is unnecessary when printing because we have overriden toString().
        // HOWEVER... if we are doing comparisons, operations or type specific tasks, getData() is required.
        System.out.println(result + " " + result.getData());

    }
}
