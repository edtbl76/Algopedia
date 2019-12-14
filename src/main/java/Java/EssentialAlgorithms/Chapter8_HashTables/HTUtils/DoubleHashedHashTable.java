package Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils;

import java.util.Random;

public class DoubleHashedHashTable {

    private int entries;
    private int used;
    private DataNugget[] table;
    private ProbeCounter probes;

    DoubleHashedHashTable() {
        this.used = 0;;
        this.probes = new ProbeCounter();
    }

    public DoubleHashedHashTable(int entries) {
        this();
        this.entries = entries;
        this.table = new DataNugget[entries];
    }

    public void add(int key, String value) {

        // 1. bail out if table full
        if (used == entries)
            throw new IndexOutOfBoundsException("Can't add key " + key + ". Table is full");

        // 2. set probe
        int probe = key % entries;

        // 3. set stride
        int stride = getStride(key);

        probes.reset();
        while (true) {
            // increment # of probes
            probes.incr();

            // 4. add if not present
            if (table[probe] == null) {
                table[probe] = new DataNugget(key, value);
                used++;
                return;
            }

            // 5. throw if dupe
            if (table[probe].getKey() == key)
                throw new IllegalArgumentException("Can't add key " + key + ". Key exists");

            // 6. throw if we've probes entries times
            if (probes.get() == entries)
                throw new IllegalArgumentException("Probe is tired.");

            // try next probe
            probe = (probe + stride) % entries;
        }
    }

    public DataNugget get(int key) {

        int probe = key % entries;
        int stride = getStride(key);

        probes.reset();
        while (true) {
            // increment # of probes
            probes.incr();

            if (table[probe] == null)
                return null;

            if (table[probe].getKey() == key)
                return table[probe];

            /*
                NOTE: order matters. if I check this before testing for membership of the key, I might
                SKIP finding the key!
             */
            if (probes.get() == entries)
                return null;

            probe = (probe + stride) % entries;
        }
    }

    private int getStride(int seed) {
        Random rand = new Random(seed);
        return rand.nextInt(entries);
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        for (int i = 0; i < entries; i++) {
            if (table[i] == null)
                sb.append("[---] ");
            else
                sb.append(table[i]).append(" ");

            if ((i + 1) % 8 == 0)
                sb.append("\n");
        }

        return String.valueOf(sb);
    }

    public double fillPercentage() {
        return 100.0 * used / entries;
    }

    public int maxLength(int min_value, int max_value) {
        int max_len = 0;
        int key = min_value;
        while(key < max_value + 1) {
            get(key);
            probes.incr();
            if (max_len < probes.get())
                max_len = probes.get();
            key++;
        }
        return max_len;
    }

    public double aveLength(int min_value, int max_value) {
        int total = 0;

        int key = min_value;
        while (key < max_value + 1) {
            get(key);
            total += probes.get();
            key++;
        }
        return total / (max_value - min_value + 1.0);
    }

}
