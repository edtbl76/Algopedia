package Java.EssentialAlgorithms.Chapter6_Sorting.ONLOGN;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.Arrays;
import java.util.stream.IntStream;

public class HeapSortExec1 {

    /**
     * HEAP - a binary tree where each node is greater than or equal to each of its child nodes.
     *      - This is also useful for priority queues, because the top of the heap is always the greatest value.
     *
     *      ROOT NODE:  always at index 0
     *
     *      CHILDREN:   for any node w/ index 'i', it has children nodes at:
     *
     *                  LEFT    = 2 x i + 1
     *                  RIGHT   = 2 x i + 2
     *
     *      PARENT      for any node w/ non-zero index 'i', it has a parent at (j - 1/ 2)
     *
     *
     *  ADDING NODES:
     *      - element are added to the bottom right most node of the tree in order to keep the  tree a "COMPLETE
     *      BINARY TREE"
     *          - Once added, the heap properties are preserved by repeatedly comparing it w/ its parent and swapping
     *          the two if it is larger.
     *
     * HEAPSORT
     *  - takes an array and builds a heap.
     *  - repeatedly swaps first and last items in the heap, rebuilding the structure (except for the last item.)
     *
     *  HEAP Sort is essentially a "cheat sort". It uses the attributes of a heap, which are that the heap is structured
     *  in a manner that removing items from the top guarantee that it is "ordered".
     *      - typically, when items are added to a heap, they are automatically sorted to preserve the property of
     *      the heap.
     *      - as items are removed, the heap automatically reconfigures itself to remain "a heap".
     *
     *      In this manner, the structure is being sorted both on insertion and selection.
     *
     * NOTE:
     *  - heapsort is "technically" the fastest comparison-based sorting algorithm
     *
     */
    public static void main(String[] args) {
        int[] array = populate(9);
        System.out.println("Initial Array: " + Arrays.toString(array));
        sort(array);
        System.out.println("Sorted Array: " + Arrays.toString(array));
    }

    private static void sort(int[] values) {

        makeHeap(values);
        System.out.println("\tArrayToHeap: " + Arrays.toString(values));

        /**
         * result of remove() is going to be the top element of the current state of the structure.
         * - this is swapped with the last element of the tree.
         *
         * The tree is going to be kept in sorted fashion as a heap (i.e. a binary tree).
         * This means that it is assorted according to tree position.
         *
         * THIS heap sort step converts a sorted heap into a sorted array.
         */
        for (int i = values.length - 1; i > 0; i--) {
            int value = remove(values, i + 1);
            System.out.println("\t\tReplacing " + values[i] + "[" + i + "] with " + value);
            values[i] = value;
        }
    }

    /**
     * This converts an array and makes it into a heap.
     */
    private static void makeHeap(int[] values) {

        for (int i = 0; i < values.length; i++) {

            int index = i;
            while (index != 0) {

                // get parent index.
                int parent = (index - 1) / 2;

                // If the kids are <= folks, then we're done.
                if (values[index] <= values[parent])
                    break;

                // If we're still here, swap kids w/ folks
                int temp = values[index];
                values[index] = values[parent];
                values[parent] = temp;

                // Move to the parent
                index = parent;
            }
        }
    }

    private static int remove(int[] values, int count) {

        int result = values[0];
        values[0] = values[count - 1];

        int index = 0;
        for ( ; ; ) {

            // Get kid nodes
            int left = 2 * index + 1;
            int right = 2 * index + 2;

            // if child is off end of the tree, use the parent index.
            if (left >= count)
                left = index;
            if (right >= count)
                right = index;

            // if the heap property is satisfied, we're done. (i..e parent is greater than kids)
            if ((values[index] >= values[left]) && (values[index] >= values[right]))
                break;

            int swap;
            if (values[left] > values[right])
                swap = left;
            else
                swap = right;

            // swap w/ bigger kid
            int temp = values[index];
            values[index] = values[swap];
            values[swap] = temp;

            // Move to kid.
            index = swap;

        }
        System.out.println("\t\tSortIteration: " + Arrays.toString(values));
        return result;
    }

    public static int[] populate(int max) {
        int[] array = new int[max];
        IntStream.rangeClosed(1, max).forEach(value -> array[value - 1] = ExecUtils.getRandom(max, 1));

        return array;
    }
}
