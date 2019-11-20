package Java.EssentialAlgorithms.Chapter2_Numbers;

import java.util.Random;

public class FermatPrimalityTest {

    public static void main(String[] args) {
        System.out.println("Number: 3, Tests: 1 " + isPrime(3, 1));
        System.out.println("Number: 569, Tests: 1 " + isPrime(569, 1));
        System.out.println("Number: 569, Tests: 10 " + isPrime(569, 10));
        System.out.println("Number: 569, Tests: 100 " + isPrime(569, 100));

    }

    private static boolean isPrime(Integer p, Integer tests) {
        // eliminate base cases
        if (p == 2)
            return true;
        if (p == 0 || p == 1 || p % 2 == 0)
            return false;

        Random random = new Random();
        for (int i = 1; i < tests; i++) {
            long test = Math.abs(random.nextInt()) % (p - 1) + 1;
            if (calculateModularExponent(test, p - 1, p) != 1)
                return false;
        }
        return true;
    }

    // (base ^ exp) % mod
    private static long calculateModularExponent(long base, long exp, long mod) {
        long result = 1;
        for (int i = 0; i < exp; i++) {
            result *= base;
            result %= mod;
        }
        return result % mod;
    }

}
