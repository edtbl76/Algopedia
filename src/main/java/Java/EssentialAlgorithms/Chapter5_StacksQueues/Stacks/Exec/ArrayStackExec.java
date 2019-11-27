package Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks.Exec;

import Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks.ArrayStack;

import java.util.stream.IntStream;

public class ArrayStackExec {
    public static void main(String[] args) {
        ArrayStack<Integer> stack = new ArrayStack<>(10);

        IntStream.rangeClosed(1, 10).forEach(value -> {
            System.out.println("Pushing: " + value);
            stack.push(value);
        });
        try {
            IntStream.rangeClosed(1, 11).forEach(value -> System.out.println("Popping: " + stack.pop()));
        } catch (ArrayIndexOutOfBoundsException ex) {
            ex.printStackTrace();
        }
    }
}
