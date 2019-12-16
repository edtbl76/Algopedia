package Java.EssentialAlgorithms.Chapter9_Recursion.BackTracking;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;



/*
    Perf Drop

    29 ~ 2 - 3 seconds
    30 ~ 77 seconds
 */
public class EightQueens3 {

    // set my vars
    //static int dimension = ExecUtils.getRandom(32, 4);
    static int dimension = 29;
    static List<List<Boolean>> boolyboard = new ArrayList<>();
    static List<List<Integer>> attacks = new ArrayList<>();

    public static void main(String[] args) {

        setupBoard();

        System.out.println("Dimensions: " + dimension);
        long start = System.nanoTime();
        if (solve(0, 0))
            printBoard();
        else
            System.out.println("No solution");
        long end = System.nanoTime();

        System.out.println("Queens: " + dimension);
        System.out.println("Time to Solve: " + TimeUnit.NANOSECONDS.toMillis(end - start));
    }

    private static void setupBoard() {
        for(int i = 0; i < dimension; i++) {
            List<Boolean> booleans = new ArrayList<>();
            List<Integer> integers = new ArrayList<>();

            for(int j = 0; j < dimension; j++) {
                booleans.add(false);
                integers.add(0);
            }
            boolyboard.add(booleans);
            attacks.add(integers);
        }
    }

    private static void printBoard() {
        StringBuilder pretty = new StringBuilder();
        boolyboard.forEach(booleans -> {
            booleans.forEach(aBoolean -> {
                if(aBoolean)
                    pretty.append("X");
                else
                    pretty.append("-");
                pretty.append(" ");
            });
            pretty.append('\n');
        });

        System.out.println(pretty);
    }

    private static boolean solve(int placed, int attempts) {
        // the easy use case... if we've placed all of the queens... we're done!
        if (placed == dimension)
            return true;

        // try positions for next queen
        /*
            This is a shortcut. No 2 queens can ever be on the same row or column.
            Since we are progressing through the board by row, then our "current" row
            reflects the queen we are trying to place.
            This is easier than iterating throw rows and cols (which has exponential time complexity)
         */
        int row = placed;
        for (int col = 0; col < dimension; col++) {

            // if there isn't a queen already here, and there are no attacks...
            if (!boolyboard.get(row).get(col) && attacks.get(row).get(col) == 0) {
                attempts++;
                boolyboard.get(row).set(col, true);

                updateAttacks(row, col, 1);

                // try others
                if (solve(placed + 1, attempts))
                    return true;

                // backtrack
                updateAttacks(row, col, -1);
                boolyboard.get(row).set(col, false);
            }
        }

        // If we get this far, we didn't find a solution.
        return false;
    }

    private static void updateAttacks(int x, int y, int adjust) {

        // mark rows, leave it ugly. YES! :)
        /*
            normally this would be refactored to be much easier to handle. I don't care right now
            I'm tired of typing.
         */

        for (int row = 0; row < dimension; row++)
            attacks.get(row).set(y, attacks.get(row).get(y) + adjust);

        // mark cols
        for (int col = 0; col < dimension; col++)
            attacks.get(x).set(col, attacks.get(x).get(col) + adjust);

        /*
            Logic Notes:
            We are using the unary '-' because we aren't counting position, we are counting
            "steps"
            - since we progress through the board by rows, marking attacks for previous rows will
            be "behind" so the step is "negative" to reflect "distance from where I am now"

            When marking the downward left > right diag (\), the columns are always after
            our current position, hence the y + i "step"

            However, when marking the upward left > right diag (/), the columns are
            before our current position, hence the y - i step.
         */

        // upper left/lower right diag
        int top_left = -Math.min(x, y);
        int btm_right = Math.min(dimension - x - 1, dimension - y - 1);

        for (int i = top_left; i <= btm_right; i++)
            attacks.get(x + i).set(y + i, attacks.get(x + i).get(y + i) + adjust);

        // lower left/upper right
        int top_right = -Math.min(x, dimension - y - 1);
        int btm_left = Math.min(dimension - x - 1, y);
        for(int i = top_right; i <= btm_left; i++)
            attacks.get(x + i).set(y - i, attacks.get(x + i).get(y - i) + adjust);

/*        System.out.println("Pos: " + x + " " + y);
        System.out.println("\\" + top_left + " " + btm_right);
        System.out.println("/" + top_right + " " + btm_left);*/
    }
}
