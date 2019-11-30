package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues;

public class LLInsertionPriorityQueue<E extends Comparable<? super E>> extends LinkedListQueue<E> {

    public LLInsertionPriorityQueue() {
        super();
    }

    LLInsertionPriorityQueue(E data) {
        super();
    }

    /**
     * This method of enqueue adds an insertion sort
     * - The purpose of the insertion sort is to keep the structure sorted for each enqueue operation.
     * - This creates a PRIORITY queue.. such that the highest priority items are always removed next.
     */
    @Override
    public void enqueue(E value) {
        super.enqueue(value);
        this.insertionSort();
    }

    public void insertionSort() {
        int items = this.size();
        int sorted = 1;
        int unsorted = items - 1;

        for (int i = 0; i < items - 1; i++) {
            // get top
            E next = this.dequeue();

            // pull other unsorted items off
            for (int j = 0; j < unsorted - 1; j++)
                super.enqueue(this.dequeue());

            // move sorted items to beginning of queue
            boolean added = false;
            for (int j = 0; j < sorted; j++) {
                E test = this.dequeue();
                if (!added && (test.compareTo(next) < 0)) {
                    // insert the larger item first
                    super.enqueue(next);
                    added = true;
                }
                super.enqueue(test);
            }
            // add next if we haven't already
            if (!added)
                super.enqueue(next);

            // manage ctrs
            sorted++;
            unsorted--;
        }
    }
}
