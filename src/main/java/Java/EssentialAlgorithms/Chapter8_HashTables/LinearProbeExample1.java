package Java.EssentialAlgorithms.Chapter8_HashTables;


import Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils.LinearHashTable;
import Java.EssentialAlgorithms.Utils.ExecUtils;

public class LinearProbeExample1 {

    public static void main(String[] args) {

        // build our HT
        int table_size = ExecUtils.getRandom(10,1);
        System.out.println("Initializing HT of size " + table_size);
        LinearHashTable table = new LinearHashTable(table_size);

        // add some data
        int keys_to_add = ExecUtils.getRandom(10, 1);
        System.out.println("Adding " + keys_to_add + " DataNugget(s)");

        int count = 0;
        while (count < keys_to_add) {
            try {
                int key = ExecUtils.getRandom(20, 1);
                String value = "v" + key;
                System.out.println("\tAdding: (" + key + ":" + value + ")");
                table.add(key, value);
                count++;
            } catch (Exception ex) {
                System.out.println(ex.getMessage());
                System.exit(1);
            }
        }

        // add/get specific key
        int one_key = ExecUtils.getRandom(20, 1);
        System.out.println("Inserting: " + one_key);

        try {
            table.add(one_key, "v" + one_key);
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
            System.exit(1);
        }

        System.out.println("Getting: " + table.get(one_key));
        System.out.print("Max Probes: ");
        System.out.println(table.getMaxLength(1, 10));
        System.out.print("Average Sequence Length: ");
        System.out.println(table.getAverageLength(1, 10));
        System.out.println("Fill Percentage: " + table.fillPercentage());

        System.out.println(table);
    }
}
