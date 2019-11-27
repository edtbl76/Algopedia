package Java.EssentialAlgorithms.Chapter4_Arrays.Matrices;

public class TriangleArray {

    private int rows;
    private int[] values;

    TriangleArray(int rows) {
        this.rows = rows;
        this.values = new int[calculateCells(rows)] ;
    }

    public int  get(int row, int col) {
        return values[rcToIndex(row, col)];
    }

    public void set(int row, int col, int value) {
        values[rcToIndex(row, col)] = value;
    }

    private int calculateCells(int rows) {
        return (rows * (rows + 1)) / 2;
    }

    private int rcToIndex(int row, int col) {
        if (row >= rows) {
            throw new IndexOutOfBoundsException("The row value " + row + " must be less than " + rows);
        }
        if (col >= rows) {
            throw new IndexOutOfBoundsException("The column value " + col + " must be less than " + rows);
        }

        // Upper to Lower Triangle
        if (col > row) {
            int temp = col;
            col = row;
            row = temp;
        }

        return calculateCells(row) + col;
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (int row = 0; row < rows; row++) {
            for(int col = 0; col <=row; col++) {
                builder
                        .append(" (").append(row)
                        .append(",").append(col)
                        .append(")=").append(get(row, col))
                        .append(" ");
            }
        }
        return String.valueOf(builder);
    }

    public TriangleArray timesFull(TriangleArray array) {
        TriangleArray result = new TriangleArray(rows);
        for(int i = 0; i < rows; i++) {
            for (int j = 0; j < rows; j++) {
                int total = 0;
                for (int k = 0; k < rows; k++) {
                    if ((i >= k) && (k >=j))
                        total += get(i, k) * array.get(k, j);
                }
                result.set(i, j, total);
            }
        }
        return result;
    }

    public TriangleArray times(TriangleArray array) {
        TriangleArray result = new TriangleArray(rows);
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < rows; j++) {
                int total = 0;
                for (int k = 0; k <= i; k++)
                    total += get(i, k) * array.get(k, j);
                result.set(i, j, total);
            }
        }
        return result;
    }
}
