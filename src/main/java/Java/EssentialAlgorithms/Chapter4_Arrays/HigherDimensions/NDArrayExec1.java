package Java.EssentialAlgorithms.Chapter4_Arrays.HigherDimensions;

import java.lang.reflect.InvocationTargetException;
import java.util.Arrays;

public class NDArrayExec1 {

    public static void main(String[] args)
            throws InvocationTargetException, NoSuchMethodException, InstantiationException, IllegalAccessException {
        int lb1 = 1, ub1 = 3;
        int lb2 = 2, ub2 = 4;
        int lb3 = 10, ub3 = 12;
        int [] bounds = new int[]{lb1, ub1, lb2, ub2, lb3, ub3};

        // Set 'Em
        NDArray<String> array = new NDArray<>(bounds, String.class);
        for (int row = lb1; row <= ub1; row++) {
            for (int col = lb2; col <= ub2; col++) {
                for (int depth = lb3; depth <= ub3; depth++) {
                    array.setValues(new int[]{row, col, depth}, row + "," + col + "," + depth);
                }
            }
        }

        // Print out the structure for posterity
        System.out.println(Arrays.toString(array.getValues()));

        // Get 'Em
        for (int row = lb1; row <= ub1; row++) {
            System.out.println("=== Row" + row + " ===");
            for (int col = lb2; col <= ub2; col++) {
                System.out.println(" Col" + col + " ===");
                for (int depth = lb3; depth <= ub3; depth++) {
                    System.out.println("  Depth" + depth + " Value: " +
                            array.get(new int[]{row, col, depth}));
                }
            }
        }


    }
}
