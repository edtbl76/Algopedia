package Java.EssentialAlgorithms.Chapter8_HashTables;

import Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils.OrderedQuadraticHashTable;
import Java.EssentialAlgorithms.Utils.ExecUtils;

public class QuadraticProbeExample2_Ordered {

    public static void main(String[] args) {
        int size = ExecUtils.getRandom(20, 4);
        OrderedQuadraticHashTable table = new OrderedQuadraticHashTable(size);
        System.out.println("Created a new ordered hash table with quadratic probing and a capacity of " + size);

        int items = ExecUtils.getRandom(size - 1, 1);
        System.out.println("Adding " + items + " data nuggets");
        for (int i = 0; i < items; i++) {
            int elem = ExecUtils.getRandom(1000, 1);
            try {
                table.add(elem, "v" + elem);
            } catch (IllegalArgumentException ignored) { }

        }

        System.out.println("Fill Percentage " + table.fillPercentage());
        System.out.println("Max Length " + table.maxLength(1, 1000));
        System.out.println("Ave Length " + table.aveLength(1, 1000));
        System.out.println(table);
        System.out.println(table.getItems());

    }
}
