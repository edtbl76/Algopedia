package Java.EssentialAlgorithms.Chapter8_HashTables;

import Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils.OrderedDoubleHashedHashTable;
import Java.EssentialAlgorithms.Utils.ExecUtils;

public class DoubleHashedExample2_Ordered {

    public static void main(String[] args) {
        int size = ExecUtils.getRandom(1000, 10);
        System.out.println("Capacity: " + size);
        OrderedDoubleHashedHashTable table = new OrderedDoubleHashedHashTable(size);

        int items = ExecUtils.getRandom(size - 1, 1);
        System.out.println("Adding " + items + " nuggets");
        for (int i = 0; i < items; i++) {
            int item = ExecUtils.getRandom(100000, 1);
            try {
                table.add(item, "v" + item);
            } catch (IllegalArgumentException ignored) { }
        }

        System.out.println("Fill Percentage " + table.fillPercentage());
        System.out.println("Max Length " + table.maxLength(1, 100000));
        System.out.println("Ave Length " + table.aveLength(1, 100000));

        System.out.println(table);
        System.out.println(table.getItems());


    }
}
