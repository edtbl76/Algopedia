package Java.EssentialAlgorithms.Chapter4_Arrays.HigherDimensions;

import java.lang.reflect.InvocationTargetException;

public class NDArray<T> {

    private T[] values;
    private int dimensions;
    private int[] lowers, slice_sizes;

    public NDArray(int[] bounds, Class<? extends T> clazz)
            throws IllegalAccessException, InstantiationException, NoSuchMethodException, InvocationTargetException {
        if ((bounds.length % 2 == 1) || (bounds.length < 2))
            throw new IllegalArgumentException();

        // init
        initialize(bounds);
    }

    /**
     * This is how we initialize an ND Array.
     * @param bounds
     */
    private void initialize(int [] bounds) {

        /**
         *  The bounds array includes the upper and lower limit for each dimension, so if we divide it by 2,
         *  we get the # of dimensions
         *  - then we create storage to hold the lower bounds and the "slice size" which holds the (upper - lower) at
         *  each dimension
         */
        this.dimensions = bounds.length / 2;
        this.lowers = new int[dimensions];
        this.slice_sizes = new int[dimensions];

        // set slice to 1. slice is the "selection" within a dimension.
        int slice_size = 1;

        /**
         * The for loop works from the top dimension down.
         * This means that we are populating 'lowers' and 'slice_sizes' from the highest index to lowest
         * - populate the slice_sizes with the size of the current slice
         * - get the value that corresponds to the lower bound of the slice we are interested in and stuff it in
         *   the lowers array to track it.
         * - get the value that corresponds to the bounds at the upper, then subtract the lower bound from that (and add 1)
         *   to get the size of that dimension.
         * - add the information to our values array.
         *
         * the next iteration is seeded w/ the bound_size we calculated.
         */
        for (int i = dimensions - 1; i >= 0; i--) {
            slice_sizes[i] = slice_size;
            lowers[i] = bounds[2 * i];
            int upper = bounds[2 * i + 1];
            int bound_size = upper - lowers[i] + 1;
            slice_size *= bound_size;
        }
        this.values = (T[])new Object[slice_size];
    }

    public void setValues(int[] indices, T value) {
        if (indices.length != dimensions)
            throw new IndexOutOfBoundsException();
        this.values[getIndex(indices)] = value;
    }

    public T[] getValues() {
        return values;
    }

    public T get(int[] indices) {
        if (indices.length != dimensions)
            throw new IndexOutOfBoundsException();
        return values[getIndex(indices)];
    }

    private int getIndex(int[] indices) {
        /**
         * The array we are provided w/ should include indices for each dimension we want to query.
         * Naturally, retrieval is tied to the initialization method.
         * - we iterate through the indices of the indices array (it contains indices!)
         * - the index of the internal "packed" array is calculated as follows
         *   - we take the index at i and subtract the stored lower bound at that index.
         *   - we multiply the result against the size of the slice at that index.
         *   - we add the index of the previous iteration (or 0 if it is the first iter).
         */
        int index = 0;
        for(int i = 0; i < indices.length; i++) {
            index += ((indices[i] - lowers[i]) * slice_sizes[i]);
        }
        return index;
    }
}

/**
 * MapToIndices Example.
 *
 * Let's say I have 3 dimensions, each with 2 values. They will be packed into the values array as follows
 *  [ 0,0,0  0,0,1  0,1,0  0,1,1  1,0,0  1,0,1  1,1,0  1,1,1 ]
 *
 *  The ROWS are the first slice. (first digit is 0 or 1)  2 Rows Total
 *  The COLS are the second slice (middle digit is 0 or 1) There are 2 cols per Row (4 total columns)
 *  The N3 is the third slice (last digit is 0 or 1). There are 2 N3s per column (8 total N3s)
 *
 */
