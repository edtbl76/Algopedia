package Java.EssentialAlgorithms.Chapter4_Arrays.TwoDArrays.Exec;

import Java.EssentialAlgorithms.Chapter4_Arrays.TwoDArrays.TwoDArray;

import java.util.Arrays;

public class TwoDArrayExec1 {

    public static void main(String[] args) {
        TwoDArray array = new TwoDArray(1, 10, 2000, 2010);

        for (int i = 1; i <= 10; i++) {
            for (int j = 2000; j <= 2010; j++) {
                array.setValues(i - 1, j - 2000,  i + "," + j);
            }
        }

        for (int i = 1; i <= 10; i++) {
            System.out.println("=== Row" + i + " ===");
            for (int j = 2000; j <= 2010; j++) {
                System.out.println(" Col" + j + " Value: " + array.get(i - 1, j - 2000));
            }
        }
    }
}
