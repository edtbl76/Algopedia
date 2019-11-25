package Java.EssentialAlgorithms.Chapter4_Arrays.TriangularArrays;

public class TriangularArray<T> {

    private int rows;
    private T[] values;

    /**
       This is a data structure that represents a connectivity matrix where there is a "diagonal" representing some
       default value where the values above the diag reflect the same values below the diag.

        This is a waste of space, so we can store only HALF of the information.
     */
    public TriangularArray(int rows) {
        this.rows = rows;
        int items = calcCells(rows);

        this.values = (T[])new Object[items];
    }

    /**
     * Given the row or column I want to find an index.
     * 1. if its out of bounds, get that sucker out of here.
     * 2. robustness principle: handle the case where someone provides me with the reflected value above the diagonal
     *    and convert it to the lower triangle.
     * 3. calculate the row coordinate and add the provided column.
     *
     *  mapping example of 5 x 5 triangular array
     *
     *     0,0
     *     1,0 1,1
     *     2,0 2,1 2,2
     *     3,0 3,1 3,2 3,3
     *     4,0 4,1 4,2 4,3 4,4
     */
    private int packToIndex(int row, int col) {
        if (row >= rows || col >= rows)
            throw new IndexOutOfBoundsException();

        /*
            Converts "Upper Triangle" to "Lower Triangle"
         */
        if (col > row) {
            int temp = col;
            col = row;
            row = temp;
        }
        return calcCells(row) + col;
    }

    /**
     * This determines the total number of cells in the array based on the number of rows we have.
     * EX: if I have 5 rows, then a standard "table" array of rows * columns, would have 25 cells.
     *
     *  The math is a little tricky here though, because technically the diagonal isn't complete.
     *  In order to truly be a diagonal, we have to reflect each row, which means taking account for the row w/ no values
     *
     *      0 0 0 0 0
     *      1 0 0 0 0
     *      1 1 0 0 0
     *      1 1 1 0 0
     *      1 1 1 1 0
     *      1 1 1 1 1
     *
     *  There are two possibles ways to calculate this:
     *
     *      cells = (rows * (rows + 1)) / 2      <--- I prefer this.
     *      cells = (rows * rows + rows) / 2
     */
    private int calcCells(int rows) {
        return (rows * (rows + 1)) / 2;
    }

    public T[] getValues() {
        return values;
    }

    public void setValues(int row, int col, T value) {
        this.values[packToIndex(row, col)] = value;
    }

    public T get(int row, int col) {
        return values[packToIndex(row, col)];
    }
}
