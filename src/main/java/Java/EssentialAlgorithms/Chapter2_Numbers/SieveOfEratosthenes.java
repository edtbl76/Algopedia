package Java.EssentialAlgorithms.Chapter2_Numbers;

import java.util.ArrayList;
import java.util.List;

public class SieveOfEratosthenes {

    public static void main(String[] args) {
        System.out.println(findPrimes(7));
        System.out.println(findPrimes(20));
        System.out.println(findPrimes(30));
        System.out.println(findPrimes(50));
        System.out.println(findPrimes(100));
        System.out.println(findPrimes(1000));
    }

    private static List<Integer> findPrimes(long max_number) {
        /*
            It's easier to use a backing array, because we need that fixed size to avoid
            all of the NPE issues.
            The alternative w/ Collections is to prefill the collection. Waste of time.
         */
        Boolean[] notPrime = new Boolean[(int)max_number + 1];

        // rule out powers of 2
        for (int i = 4; i < max_number; i += 2) {
            notPrime[i] = true;
        }

        // rule out multiples of primes so far.
        Integer next_prime = 3;
        Integer stop_at = (int) Math.sqrt(max_number);
        while (next_prime <= stop_at) {
            // ruling out the MULTIPLES.
            for (int i = next_prime * 2; i < max_number; i += next_prime) {
                notPrime[i] = true;
            }

            // move to the  next prime, skipping evens.
            next_prime += 2;
            while (next_prime <= max_number && notPrime[next_prime] != null) {
                next_prime += 2;
            }
        }
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i < max_number; i++) {
            if (notPrime[i] == null) {
                primes.add(i);
            }
        }
        return primes;
    }
}
