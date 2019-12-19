package Java.EssentialAlgorithms.Chapter9_Recursion.RecursionRemoval;

import Java.EssentialAlgorithms.Utils.ExecUtils;

public class MemoizationFibonacci2 {

    static Integer[] values = new Integer[51];
    static Integer max_values;

    public static void main(String[] args) {
        init();
        int n = ExecUtils.getRandom(50, 4);
        System.out.println("Calculating " + n + "th fibonacci: ");

        long start = System.nanoTime();
        System.out.println(fibonacci(n));
        long end = System.nanoTime();

        System.out.println("Time(ns): " + (end - start));

    }

    static void init() {
        values[0] = 0;
        values[1] = 1;
        max_values = 1;
    }

    /*
        This calculates all of the values between max_values and n on demand.
        - This yields erratic performance, because you'll be lazy loading some data and eager loading
        other data until the table is full.

        BUT... the periods are super short 20-40k ns, so its only noticed at scale.
     */
    static Integer fibonacci(Integer n) {
        if (n > max_values) {
            // Calc values between max and n.
            for (int i = max_values + 1; i <= n; i++) {
                values[i] = fibonacci(i - 1) + fibonacci(i - 2);
            }
            max_values = n;
        }
        return values[n];
    }

}
