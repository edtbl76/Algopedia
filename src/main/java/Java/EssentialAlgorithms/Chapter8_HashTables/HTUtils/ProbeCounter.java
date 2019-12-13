package Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils;

public class ProbeCounter {

    int probes = 0;

    public ProbeCounter() {
        this.probes = 0;
    }

    public void incr() {
        this.probes++;
    }

    public void set(int probes) {
        this.probes = probes;
    }

    public void reset() {
        this.set(0);
    }

    public int get() {
        return this.probes;
    }
}
