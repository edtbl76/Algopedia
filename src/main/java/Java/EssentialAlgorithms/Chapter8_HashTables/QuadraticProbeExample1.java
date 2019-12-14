package Java.EssentialAlgorithms.Chapter8_HashTables;


import Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils.QuadraticHashTable;
import Java.EssentialAlgorithms.Utils.ExecUtils;

public class QuadraticProbeExample1 {

    public static void main(String[] args) {

        int size = ExecUtils.getRandom(10, 4);
        QuadraticHashTable table = new QuadraticHashTable(size);
        System.out.println("Created HT with " + size + " slots.");

        // Different than linear probe. set maximum to be the size - 1 so that I won't overflow
        // the structure.
        int items = ExecUtils.getRandom(size - 1, 1);
        System.out.println("Adding " + items + " DataNugget(s)");
        for(int i = 0; i < items; i++) {
            int key = ExecUtils.getRandom(20, 1);
            try {
                table.add(key, "v" + key);
            } catch (IllegalArgumentException ex) {
                System.out.println("Duplicate key " + key + " not added.");
            }
        }

        // Set and retrieve
        int element = ExecUtils.getRandom(100, 21);
        try {
            System.out.println("Inserting: " + element);
            table.add(element, "v" + element);
            System.out.println("Getting: " + table.get(element));
        } catch (IndexOutOfBoundsException ex) {
            System.out.println("Too Full!");
        }


        // Stats Dump
        System.out.println("Max: " + table.getMaxLength(1, size));
        System.out.println("Average: " + table.getAverageLength(1, size));
        System.out.println("Fill Percentage: " + table.fillPercentage());

        // Table
        System.out.println(table);

    }
}
