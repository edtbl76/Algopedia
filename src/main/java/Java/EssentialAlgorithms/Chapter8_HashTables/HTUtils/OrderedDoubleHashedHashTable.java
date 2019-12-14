package Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils;

import Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils.DataNugget;
import Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils.ProbeCounter;

import javax.xml.crypto.Data;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class OrderedDoubleHashedHashTable {

    private int entries;
    private int used;
    private DataNugget[] table;
    private ProbeCounter probes;

    OrderedDoubleHashedHashTable() {
        this.used = 0;
        this.probes = new ProbeCounter();
    }

    public OrderedDoubleHashedHashTable(int entries) {
        this();
        this.entries = entries;
        this.table = new DataNugget[entries];
    }

    public void add(int key, String value) {

        // 1. if full bail
        if (used == entries)
            throw new IndexOutOfBoundsException("Can't add key " + key + ". Table is full");

        int probe = key % entries;
        int stride = getStride(key);
        int my_probes = 0;
        probes.reset();
        while (true) {

            my_probes++;
            probes.incr();

            if (table[probe] == null) {
                table[probe] = new DataNugget(key, value);
                used++;
                return;
            }

            if (table[probe].getKey() == key)
                throw new IllegalArgumentException("Can't add key " + key + ". Key Exists. Probes=" + probes.get());

            // since we are ordered we can do the swappy-wappy
            if (table[probe].getKey() > key) {

                // swappy wappy
                DataNugget old = table[probe];
                key = table[probe].getKey();
                value = table[probe].getValue();

                // rehashy
                stride = getStride(key);

                // reset my probes
                my_probes = 0;
            }

            if (my_probes == entries)
                throw new IllegalArgumentException("Couldn't find empty space to put the key");

            probe = (probe + stride) % entries;

        }
    }

    public DataNugget get(int key) {

        int probe = key % entries;
        int stride = getStride(key);

        probes.reset();
        while(true) {
            probes.incr();

            // if null or the current key from the HT is > than the given key, the key isn't present
            if (table[probe] == null || table[probe].getKey() > key) {
                return null;
            }

            if (table[probe].getKey() == key) {
                return table[probe];
            }

            if  (probes.get() == entries) {
                return null;
            }

            probe = (probe + stride) % entries;
        }
    }

    private int getStride(int seed) {
        Random rand = new Random(seed);
        return rand.nextInt(entries);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < entries; i++) {
            if (table[i] == null)
                sb.append("[-----] ");
            else
                sb.append(table[i]).append(" ");

            // (create a row for presentability)
            if ((i + 1) % 7 == 0)
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
        while (key < max_value + 1) {
            get(key);
            if (max_len < probes.get())
                max_len = probes.get();
            key++;
        }
        return max_len;
    }

    public double aveLength(int min_value, int max_value) {
        int total = 0;
        for (int key = min_value; key <= max_value; key++) {
            get(key);
            total += probes.get();
        }
        return total / (max_value - min_value + 1.0);
    }

    public List<DataNugget> getItems() {
        List<DataNugget> list = new ArrayList<>();
        for (DataNugget dn : table) {
            if (dn != null)
                list.add(dn);
        }
        return list;
    }

    public boolean scan(int key) {
        for (DataNugget dn : table) {
            if (dn.getKey() == key)
                return true;
        }
        return false;
    }
}
