package Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks.Exec;

import Java.EssentialAlgorithms.Chapter5_StacksQueues.Stacks.LinkedListStack;

import java.util.stream.IntStream;

public class LLStackExec {
    public static void main(String[] args) {
        LinkedListStack<Integer> stack = new LinkedListStack<>();
        assert stack.isEmpty();

        IntStream.rangeClosed(1, 10).forEach(value -> {
            System.out.print("Pushing: " + value + " Size: " + stack.size());
            stack.push(value);
            System.out.println("->" + stack.size());
        });
        IntStream.rangeClosed(1, 10).forEach(value -> {
            System.out.println("Popping: " + stack.pop() + " Size: " + stack.size());
        });

    }
}
