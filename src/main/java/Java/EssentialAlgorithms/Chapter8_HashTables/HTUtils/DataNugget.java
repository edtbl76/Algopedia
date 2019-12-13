package Java.EssentialAlgorithms.Chapter8_HashTables.HTUtils;

public class DataNugget {

    private int key;
    private String value;

    public DataNugget(int key, String value) {
        this.key = key;
        this.value = value;
    }

    public int getKey() {
        return key;
    }

    public String getValue() {
        return value;
    }


    @Override
    public String toString() {
        return "[" + key + ":" + value + "]";
    }
}
