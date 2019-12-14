package Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils;

public class ChainedHashTable {

    private int buckets;
    private int used;
    private Node[] list;
    private ProbeCounter sequences;


    ChainedHashTable() {
        this.used = 0;
        sequences = new ProbeCounter();
    }

    public ChainedHashTable(int buckets) {
        this();
        this.buckets = buckets;
        list = new Node[buckets];
        for(int i = 0; i < buckets; i++) {
            list[i] = new Node(Integer.MIN_VALUE, "*", null);
        }
    }

    public Node get(int key) {

        Node before = getNodeBefore(key);
        if (before == null)
            return null;

        return before.getNext();
    }

    public void add(int key, String value) {

        // if exist bail
        if (get(key) != null)
            throw new IllegalArgumentException("Key exists. [" + key + "]");

        // set head
        Node head = getBucketHead(key);
        Node node = new Node(key, value, head.getNext());
        head.setNext(node);

        used++;
    }

    public void remove(int key) {

        Node before = getNodeBefore(key);
        if (before == null)
            throw new IllegalArgumentException("Key " + key + " does not exist.");

        before.setNext(before.getNext().getNext());
        used--;
    }

    public Node getNodeBefore(int key) {

        Node head = getBucketHead(key);

        sequences.reset();
        Node node = head;
        while (node.getNext() != null) {

            sequences.incr();
            if (node.getNext().getKey() == key)
                return node;
            node = node.getNext();
        }
        // if loop completes w/o finding the key, the item isn't present
        return null;
    }

    /*
        Helper function to get the sentinel.
     */
    private Node getBucketHead(int key) {
        return list[key % buckets];
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < buckets; i++) {
            builder.append(">");
            Node node = list[i].getNext();
            while (node != null) {
                builder.append(" " + node);
                node = node.getNext();
            }
            builder.append("\n");
        }
        return String.valueOf(builder);
    }

    public double averageBucketSize() {
        return (double)used / buckets;
    }

    public int getSequenceLengths(int min, int max) {
        int maxLength = 0;
        for (int key = min; key <= max; key++) {
            get(key);
            if (maxLength < sequences.get())
                maxLength = sequences.get();
        }
        return maxLength;
    }

    public double getAverageLength(int min, int max) {
        int total = 0;
        for (int key = min; key <= max; key++) {
            get(key);
            total += sequences.get();
        }
        return total / (max - min + 1.0);
    }
}
