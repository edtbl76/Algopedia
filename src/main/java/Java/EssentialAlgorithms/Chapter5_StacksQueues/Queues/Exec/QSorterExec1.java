package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.Exec;

import Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.LLInsertionPriorityQueue;
import Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.LLSelectionPriorityQueue;
import Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues.LinkedListQueue;
import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.stream.IntStream;

public class QSorterExec1 {

    public static void main(String[] args) {

        /*
            This is a priority queue implementation that uses insertion sort. This means we sort on enqueue().
                - the structure remains sorted after each insertion, so dequeue operations (reads) are going to be
                more lightweight than writes.
         */
        LLInsertionPriorityQueue<Integer> iQueue = new LLInsertionPriorityQueue<>();
        assert iQueue.isEmpty();
        bulkNQ(iQueue, 5);
        bulkDQ(iQueue, 5);

        System.out.println();
        /*
            This is a priority queue that uses selection sort. This mean that the sort is performed on read (dequeue())
                - structure order isn't guaranteed. (in my implementation, it is POSSIBLE that the structure becomes
                sorted, because we guarantee at least one full traversal of the queue to select the largest element.
                since it swaps some of the elements.

                - each retrieval will perform "some" sorting of the structure, because I only impl'd enqueue() and dequeue().
                if i had a poll() operation, I could read each element w/o removing it... allowing me to swap only the
                largest element w/ the next element to be dequeued.
         */
        LLSelectionPriorityQueue<Integer> sQueue = new LLSelectionPriorityQueue<>();
        assert sQueue.isEmpty();
        bulkNQ(sQueue, 5);
        bulkDQ(sQueue, 5);

    }

    private static void bulkNQ(LinkedListQueue<Integer> queue, int max) {
        IntStream.rangeClosed(1, max).forEach(value -> {
                queue.enqueue(ExecUtils.getRandom(max, 1));
                System.out.println("Queue [" + queue.size() + "] " + queue);
         });
    }

    private static void bulkDQ(LinkedListQueue<Integer> queue, int max) {
        IntStream.rangeClosed(1, max).forEach(value -> {
            System.out.println("Removing: " + queue.dequeue() + "[" + queue.size() + "] " + queue);
        });
    }
}
