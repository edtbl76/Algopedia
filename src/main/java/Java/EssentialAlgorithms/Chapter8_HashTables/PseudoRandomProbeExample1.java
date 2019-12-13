package Java.EssentialAlgorithms.Chapter8_HashTables;

import Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils.PseudoRandomProbingHashTable;
import Java.EssentialAlgorithms.Utils.ExecUtils;

public class PseudoRandomProbeExample1 {

    public static void main(String[] args) {

        int size = ExecUtils.getRandom(30, 4);
        PseudoRandomProbingHashTable table = new PseudoRandomProbingHashTable(size);
        System.out.println("New Hash Table (PRProbe) with " + size + " slots");

        int items = ExecUtils.getRandom(size - 1, 2);
        System.out.println("Adding " + items + " nuggets");
        for (int i = 0; i < items; i++) {
            int element = ExecUtils.getRandom(1000, 422);
            try {
                table.add(element, "v" + element);
            } catch (IllegalArgumentException ignored) { }
        }

        System.out.println("Fill Pct " + table.getFillPercentage());
        System.out.println("Max Length " + table.maxLength(422, 1000));
        System.out.println("Ave Length " + table.aveLength(422, 1000));
        System.out.println(table);
    }
}
