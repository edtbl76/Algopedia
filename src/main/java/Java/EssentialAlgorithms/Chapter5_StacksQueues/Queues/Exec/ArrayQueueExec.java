package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.Exec;

import Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.ArrayQueue;
import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.stream.IntStream;

public class ArrayQueueExec {
    public static void main(String[] args) {
        ArrayQueue<Integer> aQueue = new ArrayQueue<>(8);

        bulkNQ(aQueue);
        System.out.println("ArrayQueue: " + aQueue);

        demoDQ(aQueue);
    }

    private static void bulkNQ(ArrayQueue<Integer> queue) {
        IntStream.rangeClosed(1,8).forEach(value -> queue.enqueue(ExecUtils.getRandom(8, 1)));
    }

    private static void demoDQ(ArrayQueue<Integer> queue) {
        IntStream.rangeClosed(1, 8).forEach(value -> {
            System.out.print("\tDequeuing: " + queue.dequeue());
            System.out.println("\tRemaining Items: [" + queue.size() + "] " + queue);
        });
    }
}
