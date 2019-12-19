package Java.EssentialAlgorithms.Chapter9_Recursion.RecursionRemoval;

import Java.EssentialAlgorithms.Utils.ExecUtils;


public class TailRecursion {

    public static void main(String[] args) {

        int n = ExecUtils.getRandom(10, 1);
        System.out.println("N = " + n);

        System.out.println("TailRecursion: ");
        long start = System.nanoTime();
        System.out.println(factorialTailRecursion(n));
        long end = System.nanoTime();
        System.out.println("Time(ns): " + (end - start));


        System.out.println("InlineTailRecursion: ");
        start = System.nanoTime();
        System.out.println(factorialTailRecursionInline(n));
        end = System.nanoTime();
        System.out.println("Time(ns): " + (end - start));

        /*
            This is actually going to run faster. (but we are talking in nanoseconds...)
         */
        System.out.println("NoTail: ");
        start = System.nanoTime();
        System.out.println(factorialNoTail(n));
        end = System.nanoTime();
        System.out.println("Time(ns): " + (end - start));

    }

    /*
        Tail Recursion
        - a scenario that occurs when the last thing a singly recursive algorithm does before returning
        is to call itself.
     */
    static int factorialTailRecursion(int n) {
        if (n == 0)
            return 1;
        int result = n * factorialTailRecursion(n - 1);
        return result;
    }

    static int factorialTailRecursionInline(int n) {
        if (n == 0)
            return 1;
        return n * factorialTailRecursion(n - 1);
    }
    /*
        This has no recursion
     */
    static int factorialNoTail(int n) {
        /*
            var to track returned value.
            - init to 1, so it can be multiplied by returned results.
         */
        int result = 1;

        /*
            Create a loop that ends w. the recursion stop condition
         */
        while (n != 0) {
            result *= n;

            n = n - 1;
        }
        return result;
    }


}
