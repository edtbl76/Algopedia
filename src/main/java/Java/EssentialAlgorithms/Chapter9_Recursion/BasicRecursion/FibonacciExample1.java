package Java.EssentialAlgorithms.Chapter9_Recursion.BasicRecursion;

import Java.EssentialAlgorithms.Utils.ExecUtils;

public class FibonacciExample1 {

    static int counter = 0;

    public static void main(String[] args) {
        int num = ExecUtils.getRandom(10, 1);
        System.out.println("Calculating fibonacci #" + num);
        System.out.println(fibonacci(num));
        System.out.println("I was called " + counter + " times");

    }

    /*
        It is painfully obvious that this isn't the best way to odo this :)
     */
    private static int fibonacci(int number) {
        counter++;
        if (number <= 1)
            return number;
        return fibonacci(number - 1) + fibonacci(number - 2);
    }
}
