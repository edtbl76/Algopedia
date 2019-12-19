package Java.EssentialAlgorithms.Chapter9_Recursion.RecursionRemoval;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.concurrent.TimeUnit;

public class MemoizationFibonacci1 {

    static int[] values = new int [100];
    static int max_values;

    public static void main(String[] args) {

        initFibonacci();
        Integer n = ExecUtils.getRandom(50, 4);
        System.out.println("Calculating the " + n + "th Fibonacci: ");

        long start = System.nanoTime();
        System.out.println(getNthFibonacci(n));
        long end = System.nanoTime();

        long result = end - start;
        if(result > 1000000)
            System.out.println("Time(ms): " + TimeUnit.NANOSECONDS.toMillis(result));
        else
            System.out.println("Time(ns): " + result);

    }

    static void initFibonacci() {
        values[0] = 0;
        values[1] = 1;
        max_values = 1;
    }

    static int getNthFibonacci(Integer n) {
        // calc if we haven't  already

        if (max_values < n) {
            /*
                NOTE: There is still recursion... but we are making the recursion more efficient.
             */
            values[n] = getNthFibonacci(n - 1) + getNthFibonacci(n - 2);
            max_values = n;
        }
        return values[n];
    }
}
