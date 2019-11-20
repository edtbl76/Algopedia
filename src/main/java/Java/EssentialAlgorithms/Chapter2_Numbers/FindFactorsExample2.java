package Java.EssentialAlgorithms.Chapter2_Numbers;

import java.util.ArrayList;
import java.util.List;

public class FindFactorsExample2 {

    public static void main(String[] args) {
        System.out.println(findFactors(10));
        System.out.println(findFactors(267));
        System.out.println(findFactors(6844));
        System.out.println(findFactors(88));

    }
    private static List<Integer> findFactors(Integer number) {
        List<Integer> factors = new ArrayList<>();
        /*
            Improvement 1:
                - check for factors of 2 first.
                cuts runtime by 50%
         */
        while (number % 2 == 0) {
            factors.add(2);
            number /= 2;
        }

        /*
            Improvement 2:
            - only check up to square root.

                if n = p * q

                    then p or q must be <= to sqrt(n)
                    reduces runtime to sqrt(n)
         */
        // check first odd factor
        Integer i = 3;
        Integer max_factor = (int) Math.sqrt(number);
        while (i <= max_factor) {
            while (number % i == 0) {
                factors.add(i);
                number /= i;
                // reset upper bound
                max_factor = (int) Math.sqrt(number);
            }
            // check next odd factor
            i += 2;
        }
        if (number > 1)
            factors.add(number);

        return factors;
    }
}
