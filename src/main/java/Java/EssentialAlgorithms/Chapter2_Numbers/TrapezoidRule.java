package Java.EssentialAlgorithms.Chapter2_Numbers;

import java.util.function.Function;
import java.util.stream.IntStream;

public class TrapezoidRule {

    public static void main(String[] args) {
        double actual = 18 - (1.0/2.0 * Math.cos(10));
        System.out.println("Actual: " + actual);

        IntStream.rangeClosed(1, 20).forEach(interval -> {
            double area = integrate(TrapezoidRule::function, 0, 5, interval);
            System.out.println("Number of Rectangles: " + interval);
            System.out.println("\tTotal Area:  " + area);
            System.out.println("\tError: " + RectangleRuleExample.getError(actual, area));
        });
    }
    
    private static double integrate(Function<Double, Double> f, double xmin, double xmax, int intervals) {
        
        // width
        double dx = (xmax - xmin) / intervals;
        
        // Get Area
        double total_area = 0;
        double x = xmin;
        for (int i = 1; i <= intervals; i++) {
            total_area = total_area + dx * (f.apply(x) + f.apply(x + dx)) / 2;
            x += dx;
        }
        return total_area;
    }
    
    private static double function(double x) {
        return 1 + x + Math.sin(2 * x);
    }
}
