package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.Exec;

import Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.LinkedListDeque;

import java.util.stream.IntStream;

public class LLDExec {
    public static void main(String[] args) {
        LinkedListDeque<Integer>  deque = new LinkedListDeque<>();

        // Seed and print
        IntStream.rangeClosed(1, 3).forEach(deque::enqueue);
        System.out.println("Seeded Deque: " + deque);

        System.out.println();
        // enq and deq normally
        deque.enqueue(4);
        System.out.println("Normal Enqueue: " + deque);
        System.out.println("Normal Dequeue: [" + deque.dequeue() + "] " + deque);

        System.out.println();
        // enq at tail, deq at head
        deque.enqueue(5, false);
        System.out.println("Enqueue@Tail: " + deque);
        System.out.println("Dequeue@Head: [" + deque.dequeue(false) + "] " + deque);

        System.out.println();
        // both at head
        deque.enqueue(6);
        System.out.println("Enqueue@Head: " + deque);
        System.out.println("Dequeue@Head: [" + deque.dequeue(false) + "] " + deque);

        System.out.println();
        // both at tail
        deque.enqueue(7, false);
        System.out.println("Enqueue@Tail: " + deque);
        System.out.println("Dequeue@Tail: [" + deque.dequeue() + "] " + deque);

    }
}
