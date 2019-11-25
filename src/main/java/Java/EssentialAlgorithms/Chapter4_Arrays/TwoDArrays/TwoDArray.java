package Java.EssentialAlgorithms.Chapter4_Arrays.TwoDArrays;

public class TwoDArray {

    private int lower1;
    private int lower2;
    private String[][] values;

    public TwoDArray(int lower1, int upper1, int lower2, int upper2) {
        this.lower1 = lower1;
        this.lower2 = lower2;

        int rows = upper1 - lower1 + 1;
        int cols = upper2 - lower2 + 1;

        /**
         *  NOTE: This can be made generic w/ Supplier or Class + reflection via Array.newInstance().
         *  However, that defeats the purpose of demonstrating multi-dimension arrays for now.
         */
        this.values = new String[rows][cols];
    }

    public void setValues(int row, int col, String values) {
        this.values[row][col] = values;
    }

    public String[][] getValues() {
        return values;
    }

    public String get(int row, int col) {
        return values[row][col];
    }
}
