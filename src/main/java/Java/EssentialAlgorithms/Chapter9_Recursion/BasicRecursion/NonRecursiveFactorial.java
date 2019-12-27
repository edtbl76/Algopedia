package Java.EssentialAlgorithms.Chapter9_Recursion.BasicRecursion;

import Java.EssentialAlgorithms.Utils.ExecUtils;

public class NonRecursiveFactorial {

    public static void main(String[] args) {

        int n = ExecUtils.getRandom(10, 1);
        System.out.println("Factorial of " + n + ":");
        System.out.println(factorial(n));
    }

    static long factorial(int n) {

        long result = 1;
        while (n != 0) {
            result *= n;
            n--;
        }
        return result;
    }
}
