package Java.EssentialAlgorithms.Chapter9_Recursion.BasicRecursion;

import Java.EssentialAlgorithms.Utils.ExecUtils;

public class FactorialExample {

    static int counter = 0;
    public static void main(String[] args) {
        int start = ExecUtils.getRandom(10, 1);
        System.out.println("Factorial of " + start + " is " + factorial(start));
        System.out.println("I was called " + counter + " times");
    }

    /*
        Time complexity = O(N), because we have to traverse all of the numbers to make the calculation
        Recursion Depth = N + 1 (i.e the initial call + each mult operation)
     */
    private static Integer factorial(int n) {
        counter++;
        if (n == 0)
            return 1;
        else
            return n * factorial(n - 1);
    }
}
