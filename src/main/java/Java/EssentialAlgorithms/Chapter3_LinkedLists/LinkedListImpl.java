package Java.EssentialAlgorithms.Chapter3_LinkedLists;

public class LinkedListImpl {

    /**
     *  Demonstrates LLImplExec1
     */
    public static void iterate(Cell<?> cell) {
        while (cell != null) {
            System.out.println(cell);
            cell = cell.getNext();
        }
    }

    /**
     * Demonstrates LLImplExec2
     */
    public static <E extends Comparable<E>> Cell<E> findCell(Cell<E> cell, E data) {
        while (cell != null) {
            if (cell.getData().equals(data))
                return cell;

            cell = cell.getNext();
        }
        return null;
    }

    /**
     * Demonstrates LLImplExec3
     * NOTE: we can never return the first value!!!!!
     */
    public static <E extends Comparable<E>> Cell<E> findCellBefore(Cell<E> cell, E data) {
        if (cell == null)
            return null;

        while (cell.getNext() != null) {
            /*
                Important. You can't use == to compare these. equals() is used for value comparison.
                == is used if they point to the same memory location.
             */
            if (cell.getNext().getData().equals(data)) {
                return cell;
            }
            cell = cell.getNext();
        }
        return null;
    }
}
