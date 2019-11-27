package Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks.Exec;

import Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks.ArrayStack;

import java.util.stream.IntStream;

public class ReverseArrayWithStack {
    public static void main(String[] args) {
        ArrayStack<Integer> stack = new ArrayStack<>(10);

        IntStream.rangeClosed(1, 10).forEach(stack::push);
        System.out.println("Stack (Top To Bottom): " + stack);

        ArrayStack<Integer> countdown = new ArrayStack<>(10);
        IntStream.rangeClosed(1, 10).forEach(value -> {
            countdown.push(stack.pop());
        });
        System.out.println("Final Countdown: " + countdown);


    }
}
