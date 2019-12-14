package Java.EssentialAlgorithms.Chapter8_HashTables;

import Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils.ChainedHashTable;
import Java.EssentialAlgorithms.Utils.ExecUtils;

public class ChainedHTExample1 {
    public static void main(String[] args) {

        int size = ExecUtils.getRandom(10, 4);
        System.out.println("Creating Chained HashTable with " + size + " buckets");
        ChainedHashTable table = new ChainedHashTable(size);

        int items = ExecUtils.getRandom(50 , 1);
        System.out.println("Adding " + items + " Node(s)");
        for(int i = 0; i < items; i++) {
            int key = ExecUtils.getRandom(99, 1);
            try {
                table.add(key, "v" + key);
            } catch(IllegalArgumentException ex) {
                System.out.println("Duplicate key " + key + " found. Skipping");
            }
        }

        System.out.println("Average Bucket Size: " + table.averageBucketSize());
        System.out.println("Max Length: " + table.getSequenceLengths(1, 99));
        System.out.println("Ave Length: " + table.getAverageLength(1, 99));
        System.out.println(table);

    }
}
