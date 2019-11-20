package Java.EssentialAlgorithms.Chapter2_Numbers;

public class EuclidianAlgorithm {

    public static void main(String[] args) {
        System.out.println("=== Without Recursion ===");
        System.out.println(gcd(100, 20));
        System.out.println(gcd(4851, 3003));

        System.out.println("=== With Recursion ===");
        System.out.println(gcdRecurse(100, 20));
        System.out.println(gcdRecurse(4851, 3003));

    }

    private static int gcd(int p, int q) {
        while (q != 0) {
            int temp = q;
            q = p % q;
            p = temp;
        }
        return p;
    }

    private static int gcdRecurse(int p, int q) {
        if (q == 0)
            return p;
        else
            System.out.println("\tValues: " + p + " " + q + " " + p % q);
            return gcdRecurse(q, p % q);
    }

}
