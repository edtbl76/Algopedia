package Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils;

import java.util.Random;

public class PseudoRandomProbingHashTable {

    private int entries;
    private int used;
    private DataNugget[] table;
    private ProbeCounter probes;

    PseudoRandomProbingHashTable() {
        this.used = 0;
        this.probes = new ProbeCounter();
    }

    public PseudoRandomProbingHashTable(int entries) {
        this();
        this.entries = entries;
        this.table = new DataNugget[entries];
    }

    public void add(int key, String value) {

        // is table full
        if (used == entries)
            throw new IndexOutOfBoundsException("Table full. Can't add key " + key);

        int probe = key % entries;

        //
        int stride = getStride(probe);

        probes.reset();
        while (true) {
            probes.incr();

            // if empty, add and bail
            if (table[probe] == null) {
                table[probe] = new DataNugget(key, value);
                used++;
                return;
            }

            // tired yet?
            if (probes.get() == entries)
                throw new IllegalArgumentException("Can't add key " + key + ". No empty slots found.");

            probe = (probe + stride) % entries;
        }
    }

    public DataNugget get(int key) {

        int probe = key % entries;
        int stride = getStride(probe);

        probes.reset();
        while(true) {
            probes.incr();

            if(table[probe] == null)
                return null;

            if(table[probe].getKey() == key)
                return table[probe];

            if(probes.get() == entries)
                return null;

            probe = (probe + stride) % entries;
        }
    }

    public int getStride(int seed) {
        Random rand = new Random(seed);
        return rand.nextInt(entries);
    }

    @Override
    public String toString() {
        StringBuilder sb =  new StringBuilder();
        for(int i = 0; i < entries; i++) {
            if (table[i] == null)
                sb.append("[-------] ");
            else
                sb.append(table[i]).append(" ");

            if ((i + 1) % 10 == 0)
                sb.append("\n");
        }
        return String.valueOf(sb);
    }

    public double getFillPercentage() {
        return 100.0 * used / entries;
    }

    public int maxLength(int min_value, int max_value) {
        int max_length = 0;
        for(int i = min_value; i <= max_value; i++) {
            get(i);
            if(max_length < probes.get())
                max_length = probes.get();
        }
        return max_length;
    }

    public double aveLength(int min_value, int max_value) {
        int total = 0;
        for (int i = min_value; i <= max_value; i++) {
            get(i);
            total += probes.get();
        }
        return total / (max_value - min_value + 1.0);
    }
}
