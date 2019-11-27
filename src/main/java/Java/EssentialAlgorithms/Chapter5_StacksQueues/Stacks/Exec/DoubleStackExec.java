package Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks.Exec;

import Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks.DoubleStack;

import java.util.stream.IntStream;

public class DoubleStackExec {
    public static void main(String[] args) {
        DoubleStack<Integer> stack = new DoubleStack<>(10);

        IntStream.rangeClosed(1, 5).forEach(value -> {
            System.out.println("Pushing " + value);
            stack.pushTop(value);
            stack.pushBottom(value);
        });

        IntStream.rangeClosed(1, 5).forEach(value -> {
            System.out.println("Popping " + stack.popTop() + " from the Top");
            System.out.println("Popping " + stack.popBottom() + " from the Bottom");
        });

    }
}
