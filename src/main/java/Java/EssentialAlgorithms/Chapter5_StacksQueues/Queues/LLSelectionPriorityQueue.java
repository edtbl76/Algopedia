package Java.EssentialAlgorithms.Chapter5_StacksQueues.Queues;

public class LLSelectionPriorityQueue<E extends Comparable<? super E>> extends LinkedListQueue<E> {

    public LLSelectionPriorityQueue() {
        super();
    }

    public LLSelectionPriorityQueue(E data){
        super();
    }

    @Override
    public E dequeue() {
        return getLargest(this.size());
    }

    /**
     * Doing a FULL selection Sort for this is probably overkill. We don't need to sort the structure (although it is
     * an Eager sort for future selections sort of.)
     *
     */
    private void selectionSort() {
        int items = this.size();
        int sorted = 0;
        int unsorted = items;
        for(int i = 0; i < items; i++) {

            super.enqueue(getLargest(unsorted));
            for(int j = 0; j < unsorted; j++) {
                super.enqueue(super.dequeue());
            }

            sorted++;
            unsorted--;
        }
    }

    /**
     * If I pass in the size of the queue, this will find the largest item. This is a better way to deal w/
     * performing PriorityQueue on dequeue operations
     */
    private E getLargest(int items) {
        E biggest = super.dequeue();
        for (int i = 0; i < items - 1; i++) {
            E test = super.dequeue();
            if (test.compareTo(biggest) > 0) {
                super.enqueue(biggest);
                biggest = test;
            } else {
                super.enqueue(test);
            }
        }
        // Whatever we have at "biggest" right now is in a temp variable. we don't need to add it
        // back to the queue unless we are doing a full sort operation.
        return biggest;
    }
}
