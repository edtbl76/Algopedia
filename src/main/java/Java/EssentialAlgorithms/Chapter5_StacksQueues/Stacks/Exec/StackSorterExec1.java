package Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks.Exec;

import Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks.StackSorter;
import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Stack;
import java.util.stream.IntStream;

public class StackSorterExec1 {
    public static void main(String[] args) {

        // Create Stacks
        Stack<Integer> stack1 = new Stack<>();
        Stack<Integer> stack2 = new Stack<>();

        // Seed it
        bulkPush(stack1);
        bulkPush(stack2);

        // Demo Insertion Sort
        System.out.println("Unsorted Content Stack1: " + stack1.toString());
        StackSorter<Integer> iSorter = new StackSorter<>(stack1);
        iSorter.insertionSort();
        System.out.println("Sorted Content (Insertion) : " + stack1.toString());

        System.out.println();
        // Demo Selection Sort
        System.out.println("Unsorted Content Stack2: " + stack2.toString());
        StackSorter<Integer> sSorter = new StackSorter<>(stack2);
        sSorter.selectionSort();
        System.out.println("Sorted Content (Selection) : " + stack2.toString());

    }

    private static void bulkPush(Stack<Integer> stack) {
        IntStream.rangeClosed(1, 10).forEach(value -> stack.push(ExecUtils.getRandom(10, 1)));
    }


}
