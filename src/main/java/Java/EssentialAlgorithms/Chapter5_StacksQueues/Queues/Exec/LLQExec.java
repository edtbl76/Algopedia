package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.Exec;

import Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.LinkedListQueue;
import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.stream.IntStream;

public class LLQExec {
    public static void main(String[] args) {
        LinkedListQueue<Integer> queue = new LinkedListQueue<>();
        assert queue.isEmpty();

        bulkNQ(queue);
        System.out.println("Populated Queue: " + queue);

        demoDQ(queue);

    }

    private static void bulkNQ(LinkedListQueue<Integer> queue) {
        IntStream.rangeClosed(1, 5).forEach(value -> queue.enqueue(ExecUtils.getRandom(5, 1)));
    }

    private static void demoDQ(LinkedListQueue<Integer> queue) {
        IntStream.rangeClosed(1, 5).forEach(value -> {
            System.out.print("\tDequeuing: " + queue.dequeue());
            System.out.println("\tRemaining Items: [" + queue.size() + "] " + queue);
        });
    }
}
