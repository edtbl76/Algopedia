package Java.EssentialAlgorithms.Chapter9_Recursion.RecursionRemoval;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.concurrent.TimeUnit;

public class MemoizationFibonacci3 {

    static Integer[] values = new Integer[51];

    public static void main(String[] args) {
        long start = System.nanoTime();
        init();
        long end = System.nanoTime();


        long initTime = end - start;
        if (initTime < 1000000)
            System.out.println("Initialization took " + initTime + " ns");
        else
            System.out.println("Initialization took " + TimeUnit.NANOSECONDS.toMillis(initTime) + " ms");

        int n = ExecUtils.getRandom(50, 4);
        System.out.println("Calculating " + n + "th fibonacci: ");

        start = System.nanoTime();
        System.out.println(fibonacci(n));
        end = System.nanoTime();

        System.out.println("Time(ns): " + (end - start));

    }

    static void init() {
        values[0] = 0;
        values[1] = 1;

        for(int i = 2; i < values.length; i++) {
            values[i] = fibonacci(i - 1) + fibonacci(i - 2);
        }
    }

    /*
        This answers the problem of version 2:
        - we frontload the seeding of the table, which still takes under 100k ns (which is 1/100th of a millisecond)
        - this optimizes our retrieval time, but it also gives us consistency.. i.e. as far as the code is concerned,
        all retrievals are equal (within the given data type).
     */
    static Integer fibonacci(Integer n) {
        return values[n];
    }

}
