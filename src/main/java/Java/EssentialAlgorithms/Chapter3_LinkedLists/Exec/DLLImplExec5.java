package Java.EssentialAlgorithms.Chapter3_LinkedLists.Exec;

import Java.EssentialAlgorithms.Chapter3_LinkedLists.Cell;
import Java.EssentialAlgorithms.Chapter3_LinkedLists.DoublyLinkedListImpl;

import java.util.Arrays;
import java.util.Iterator;

public class DLLImplExec5 {

    public static void main(String[] args) {
        DoublyLinkedListImpl<Integer> list = new DoublyLinkedListImpl<>(Arrays.asList(1, 2, 3, 4, 5));
        System.out.println("Size: " + list.size() + " Content: [" + list + "]");

        // Forward (Iterator<> interface doesn't go backwards :P)
        Iterator<Integer> iterator = list.iterator();
        while (iterator.hasNext())
            System.out.println(iterator.next());

        DoublyLinkedListImpl<Integer> mess = new DoublyLinkedListImpl<>(Arrays.asList(
                101, 3, 85, 62, 4, 9765, 22, 18, 4, 2, 26, 44, 8));
        System.out.println("Size: " + mess.size() + " Content: [" + mess+ "]");

        DoublyLinkedListImpl<Integer> cleaned = insertionSort(mess);
        System.out.println("Size: " + cleaned.size() + " Content: [" + cleaned + "]");



    }

    private static DoublyLinkedListImpl<Integer> insertionSort(DoublyLinkedListImpl<Integer> input) {
        // Step ONE... set up some storage
        DoublyLinkedListImpl<Integer> sorted = new DoublyLinkedListImpl<>();

        // Create an iterator for input
        Iterator<Integer> inputIter = input.iterator();
        while(inputIter.hasNext()) {
            sorted.insertSorted(inputIter.next());
        }
        return sorted;
    }

}
