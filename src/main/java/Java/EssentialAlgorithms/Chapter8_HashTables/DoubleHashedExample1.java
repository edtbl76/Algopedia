package Java.EssentialAlgorithms.Chapter8_HashTables;

import Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils.DoubleHashedHashTable;
import Java.EssentialAlgorithms.Utils.ExecUtils;

public class DoubleHashedExample1 {

    public static void main(String[] args) {

        int size = ExecUtils.getRandom(100, 4);
        System.out.println("Creating a DoubleHash Hash Table with a capacity of " + size);
        DoubleHashedHashTable table = new DoubleHashedHashTable(size);

        int items = ExecUtils.getRandom(size - 1, 1);
        System.out.println("Adding " + items + " nuggets");
        for (int i = 0; i < items; i++) {
            int item = ExecUtils.getRandom(9999, 1);

            // blowing off the dupes.
            try {
                table.add(item, "v" + item);
            } catch (IllegalArgumentException ignored) { }
        }

        System.out.println("Fill Pct " + table.fillPercentage());
        System.out.println("Max Length " + table.maxLength(1, 9999));
        System.out.println("Ave Length " + table.aveLength(1, 9999));
        System.out.println(table);
    }
}
