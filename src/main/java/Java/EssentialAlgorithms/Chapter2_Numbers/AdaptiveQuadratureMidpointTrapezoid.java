package Java.EssentialAlgorithms.Chapter2_Numbers;

import java.util.function.Function;

public class AdaptiveQuadratureMidpointTrapezoid {

    private static int count = 2;

    public static void main(String[] args) {
        double actual = 18 - (1.0/2.0 * Math.cos(10));
        System.out.println("Actual: " + actual);

        double pct = 1.0;
        while (pct != .00001) {
            double area = integrate(AdaptiveQuadratureMidpointTrapezoid::function, 0, 5, 2, pct);

            System.out.println("Total Area: " + area);
            System.out.println("\tMaxError: " + pct);
            System.out.println("\tError: " + RectangleRuleExample.getError(actual, area));
            System.out.println("\tResulting Rectangles: " + count);
            pct /= 10;
        }
    }

    public static double integrate(
            Function<Double, Double> f, double xmin, double xmax, int intervals, double max_error) {

        // get width of initial traps
        double dx = (xmax - xmin) / intervals;

        // get the area
        double total_area = 0;
        double x = xmin;
        for (int i = 1; i <= intervals; i++) {
            total_area = total_area + getSliceArea(f, x, x + dx, max_error);
            x = x + dx;
        }
        return total_area;
    }

    public static double getSliceArea(Function<Double, Double> f, double x1, double x2, double max_error) {
        double midpoint = (x1 + x2) / 2;

        // calculate function at endpoints and midpoint
        double y1 = f.apply(x1);
        double y2 = f.apply(x2);
        double ymid =  f.apply(midpoint);

        // get area of whole and parts
        double area_calc = (x2 - x1) * (y1 + y2) / 2.0;
        double area_left = (midpoint - x1) * (y1 + ymid) / 2.0;
        double area_right = (x2 - midpoint) * (ymid + y2) / 2.0;
        double area_sum = area_left + area_right;

        // how close
        double error = (area_sum - area_calc) / area_calc;

        // Manage error allowance
        if (Math.abs(error) < max_error) {
            return area_calc;
        } else {
            count += 1;
            return getSliceArea(f, x1, midpoint, max_error) + getSliceArea(f, midpoint, x2, max_error);
        }
    }

    private static double function(double x) {
        return 1 + x + Math.sin(2 * x);
    }
}
