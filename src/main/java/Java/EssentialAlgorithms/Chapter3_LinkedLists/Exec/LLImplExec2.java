package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.Cell;
import Java.EssentialAlgorithms.Chapter3_LinkedLists.LinkedListImpl;

public class LLImplExec2 {

    public static void main(String[] args) {
        // Set up 2 cells. Here I demonstrate default constructor and one that initializes the cell w/ data.
        Cell<String> cell = new Cell<>("name");
        Cell<String> otherCell = new Cell<>();
        otherCell.setData("address");

        // Build the List by wiring the two cells together.
        cell.setNext(otherCell);

        // Test Case
        Cell<String> name = LinkedListImpl.findCell(cell, "name");
        System.out.println(name.getData());
    }
}
