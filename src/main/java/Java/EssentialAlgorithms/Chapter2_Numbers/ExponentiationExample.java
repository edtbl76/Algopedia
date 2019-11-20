package Java.EssentialAlgorithms.Chapter2_Numbers;

public class ExponentiationExample {

    public static void main(String[] args) {
        System.out.println(exponentiate(2, 0));
        System.out.println(exponentiate(2, 1));
        System.out.println(exponentiate(5, 2));
        System.out.println(exponentiate(7, 4));
        System.out.println(exponentiate(7, 6));

    }

    private static double exponentiate(double base, long exp) {
        System.out.println("\tEquation: " + base + "^" + exp);
        if (exp < 0 || base < 0)
            return -1;
        if (exp == 0)
            return 1;
        if (exp == 1)
            return base;
        if (exp == 2)
            return base * base;

        if (exp % 2 == 0)
            return exponentiate(exponentiate(base, exp / 2), 2);
        else
            return base * exponentiate(exponentiate(base, (exp - 1)/ 2), 2);
    }
}
