package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.Exec;

import Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.CircularArrayQueue;
import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.stream.IntStream;

public class CAQExec {
    public static void main(String[] args) {
        CircularArrayQueue<Integer> aQueue = new CircularArrayQueue<>(9);

        // First Run
        bulkNQ(aQueue, 5);
        System.out.println("ArrayQueue: " + aQueue);
        demoDQ(aQueue, 3);

        // Second
        bulkNQ(aQueue,4);
        System.out.println("ArrayQueue: " + aQueue);
        demoDQ(aQueue, 4);

        // Third
        bulkNQ(aQueue, 6);
        System.out.println("ArrayQueue: " + aQueue);
        demoDQ(aQueue, 8);


    }

    private static void bulkNQ(CircularArrayQueue<Integer> queue, int max) {
        IntStream.rangeClosed(1, max).forEach(value -> queue.enqueue(ExecUtils.getRandom(max, 1)));
    }

    private static void demoDQ(CircularArrayQueue<Integer> queue, int max) {
        IntStream.rangeClosed(1, max).forEach(value -> {
            System.out.print("\tDequeuing: " + queue.dequeue());
            System.out.println("\tRemaining Items: [" + queue.size() + "] " + queue);
        });
    }
}
