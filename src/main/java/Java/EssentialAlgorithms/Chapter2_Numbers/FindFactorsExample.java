package Java.EssentialAlgorithms.Chapter2_Numbers;

import java.util.ArrayList;
import java.util.List;

public class FindFactorsExample {

    public static void main(String[] args) {
        System.out.println(findFactors(10));
        System.out.println(findFactors(267));
        System.out.println(findFactors(6844));
        System.out.println(findFactors(88));

    }

    private static List<Integer> findFactors(Integer number) {
        List<Integer> factors = new ArrayList<>();
        Integer i = 2;
        while (i < number) {
            while(number % i == 0) {
                factors.add(i);
                number /= i;
            }
            i += 1;
        }
        if (number > 1)
            factors.add(number);
        return factors;
    }
}
