package Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils;

import java.util.ArrayList;
import java.util.List;

public class OrderedQuadraticHashTable {

    private int entries;
    private int uses;
    private DataNugget[] table;
    private ProbeCounter probes;

    OrderedQuadraticHashTable() {
        this.uses = 0;
        probes = new ProbeCounter();
    }

    public OrderedQuadraticHashTable(int entries) {
        this();
        this.entries = entries;
        table = new DataNugget[entries];
    }

    public void add(int key, String value) {

        // bail if table is full
        if (uses == entries)
            throw new IllegalArgumentException("Table is full. Can't add key: " + key);

        int probe = key % entries;
        probes.reset();

        while (true) {
            probes.incr();

            // add if empty
            if (table[probe] == null) {
                table[probe] = new DataNugget(key, value);
                uses++;
                return;
            }

            // bail if exists
            if (table[probe].getKey() == key)
                throw new IllegalArgumentException("Key " + key + " exists.");

            // keep going until we hit larger key
            /*
                This is how we keep the structure ordered.
             */
            if (table[probe].getKey() > key) {

                // swap values
                DataNugget old = table[probe];
                table[probe] = new DataNugget(key, value);
                key = old.getKey();
                value = old.getValue();

                // Rehash Larger Item
                int temp = probes.get();
                this.add(key, value);
                probes.set(probes.get() + temp);
                return;
            }

            // bounds failure
            if (probes.get() == entries)
                throw new IllegalArgumentException("Can't add key " + key + ". Unable to locate empty slot");

            // update probe
            probe = (key + probes.get() * probes.get()) % entries;
        }

    }

    public DataNugget get(int key) {

        int probe = key % entries;

        probes.reset();
        while (true) {
            probes.incr();

            // if spot is empty or key is larger than new key, it isn't here.
            if (table[probe] == null || table[probe].getKey() > key)
                return null;

            // did we find it?
            if (table[probe].getKey() == key)
                return table[probe];

            // are we exhausted?
            if (probes.get() == entries)
                return null;

            // next!
            probe = (key + probes.get() * probes.get()) % entries;
        }
    }

    @Override
    public String toString() {
        StringBuilder text = new StringBuilder();
        for (int i = 0; i < entries; i++) {
            if(table[i] == null)
                text.append("[-------] ");
            else
                text.append(table[i]).append(" ");

            if ((i + 1) % 10 == 0)
               text.append("\n");
        }
        return String.valueOf(text);
    }

    public double fillPercentage() {
        return (double)100 * uses / entries;
    }

    public int maxLength(int min_value, int max_value) {
        int max_len = 0;
        for (int key = min_value; key <= max_value; key++) {
            get(key);
            if (max_len < probes.get())
                max_len = probes.get();
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
        List<DataNugget> list =  new ArrayList<>();
        for (DataNugget dataNugget : table) {
            if (dataNugget != null)
                list.add(dataNugget);
        }
        return list;
    }

    public boolean scanTable(int key) {
        for (DataNugget dn : table) {
          if ((dn != null) && (dn.getKey() == key))
              return true;
        }
        return false;
    }
}
