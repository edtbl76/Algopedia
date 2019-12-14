package Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils;

public class QuadraticHashTable {

    private int entries;
    private int used;

    public ProbeCounter sequences;

    private DataNugget[] table;

    QuadraticHashTable() {
        this.used = 0;
        sequences = new ProbeCounter();
    }

    public QuadraticHashTable(int entries) {
        this();
        this.entries = entries;
        table = new DataNugget[this.entries];
    }

    public void add(int key, String value) {

        if(used == entries)
            throw new IndexOutOfBoundsException("Cannot add key " + key + ". Table is full");


        int probe = key % entries;
        int stride = 1;
        sequences.reset();
        for (;;) {
            sequences.incr();

            // empty slot equals put it in the pot!
            if (table[probe] == null) {
                table[probe] = new DataNugget(key, value);
                used++;
                return;
            }

            // check for uniqueness
            if (table[probe].getKey() == key)
                throw new IllegalArgumentException(
                        "Key " + key + " exists at index " + probe + ". (" + sequences.get() + ") probes"
                );

            // Quadratic probe uses square of stride for each step.
            probe = (probe + (stride * stride)) % entries;
        }
    }

    public DataNugget get(int key) {
        int probe = key % entries;
        int stride = 1;

        sequences.reset();
        for (;;) {
            sequences.incr();

            // STOP! it ain't here :)
            if (table[probe] == null)
                return null;

            if (table[probe].getKey() == key)
                return table[probe];

            // if we are full, don't move to next iteration.
            if (sequences.get() == entries)
                return null;

            probe = (probe + (stride * stride)) % entries;
        }
    }

    public double fillPercentage() {
        return 100.0 * used / entries;
    }

    public int getMaxLength(int min_value, int max_value) {
        int max = 0;
        for (int key = min_value; key <= max_value; key++) {
            sequences.get();
            get(key);
            sequences.incr();
            if (max < sequences.get())
                max = sequences.get();
        }
        return max;
    }

    public double getAverageLength(int min_value, int max_value) {

        int total = 0;
        for(int key = min_value; key <= max_value; key++) {
            total++;
        }
        return total / (max_value - min_value + 1.0);
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < entries; i++) {
            if (table[i] == null)
                builder.append("[--------] ");
            else
                builder.append(table[i] );

            if((i + 1) % 10 == 0)
                builder.append("\n");
        }

        return String.valueOf(builder);
    }
}
