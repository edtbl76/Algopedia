package Java.EssentialAlgorithms.Chapter4_Arrays.TriangularArrays;

import java.util.Arrays;

public class Example {

    public static void main(String[] args) {
        TriangularArray<String> array = new TriangularArray<>(5);

        // Build it!
        for(int row = 0; row < 5; row++) {
            for(int col = 0; col <= row; col++) {
                array.setValues(row, col, "(" + row + "," + col + ")");
            }
        }

        // Display structure for posterity
        System.out.println(Arrays.toString(array.getValues()));

        // get each
        for(int row = 0; row < 5; row++) {
            System.out.println("=== Row" + row + " ===");
            for(int col = 0; col <= row; col++) {
                System.out.println("  Col" + col + " Value: " + array.get(row, col));
            }
        }

    }
}
