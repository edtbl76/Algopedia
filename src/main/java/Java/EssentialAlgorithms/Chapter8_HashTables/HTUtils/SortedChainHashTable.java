package Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils;

public class SortedChainHashTable {

    private int buckets;
    private int used;
    private Node[] list;
    private ProbeCounter sequences;

    SortedChainHashTable() {
        this.used = 0;
        this.sequences = new ProbeCounter();
    }

    public SortedChainHashTable(int buckets) {
        this();
        this.buckets = buckets;
        list = new Node[buckets];
        for (int i = 0; i < buckets; i++) {
            Node tail = new Node(Integer.MAX_VALUE, "*", null);
            list[i] = new Node(Integer.MIN_VALUE, "*", tail);
        }
    }

    public void add(int key, String value) {
        Node before = findNodeBefore(key);
        sequences.incr();

        // make sure not already present
        if (before.getNext().getKey() == key)
            throw new IllegalArgumentException("Key exists. [" + key + "]");

        // add
        Node node = new Node(key, value, before.getNext());
        before.setNext(node);
        used++;
    }

    public void remove(int key) {
        Node before = findNodeBefore(key);

        if (before.getNext().getKey() != key)
            throw new IllegalArgumentException("Key "+ key + " doesn't exist");

        sequences.incr();
        before.setNext(before.getNext().getNext());
        used--;
    }

    public Node find(int key) {
        Node before = findNodeBefore(key);
        sequences.incr();

        if (before.getNext().getKey() != key)
            return null;
        return before.getNext();
    }

    public Node findNodeBefore(int key) {

        Node head = list[key % buckets];
        sequences.reset();
        Node node  = head;

        /*
            The difference between this logic and a "normal" chain is that
            we can take advantage of the sorted structure, so we can stop once we find
            a key that is larger.
        */
        while (node.getNext().getKey() < key) {
            sequences.incr();
            node = node.getNext();
        }
        return node;
    }


    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        builder.append(">");
        for (int i = 0; i < buckets; i++) {
            builder.append(">");
            Node node = list[i].getNext();
            while (node.getKey() != Integer.MAX_VALUE) {
                builder.append(" " + node);
                node = node.getNext();
            }
            builder.append("\n");
        }
        return String.valueOf(builder);
    }

    public double averageBucketSize() {
        return used / (double)buckets;
    }

    public int maxSequenceLength(int min_value, int max_value) {
        int max_len = 0;
        for(int key = min_value; key <= max_value; key++) {
            find(key);
            if (max_len < sequences.get())
                max_len = sequences.get();
        }
        return max_len;
    }

    public double aveSequenceLength(int min_value, int max_value) {
        int total = 0;
        for(int key = min_value; key <= max_value; key++) {
            find(key);
            total += sequences.get();
        }

        return total / (max_value - min_value + 1.0);
    }
}
