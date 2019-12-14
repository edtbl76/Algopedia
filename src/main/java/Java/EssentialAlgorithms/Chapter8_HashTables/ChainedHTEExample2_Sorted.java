package Java.EssentialAlgorithms.Chapter8_HashTables;

import Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils.SortedChainHashTable;
import Java.EssentialAlgorithms.Utils.ExecUtils;

public class ChainedHTEExample2_Sorted {

    public static void main(String[] args) {
        int size = ExecUtils.getRandom(8, 4);
        System.out.println("Creating a sorted chain HT with " + size + " buckets");
        SortedChainHashTable table = new SortedChainHashTable(size);

        int items = ExecUtils.getRandom(size - 1, 1);
        System.out.println("Adding " + items + " nodes");
        for (int i = 0; i < items; i++) {
            int element = ExecUtils.getRandom(1000, 1);
            try {
                table.add(element, "v" + element);
            } catch (IllegalArgumentException ex) {
                System.out.println("Duplicate key (" + element + ") found. Skipping");
            }
        }

        System.out.println("Ave Bucket Size: " + table.averageBucketSize());
        System.out.println("Max Sequence Length: " + table.maxSequenceLength(1,1000));
        System.out.println("Ave Sequence Length: " + table.aveSequenceLength(1,1000));
        System.out.println(table);
    }
}
