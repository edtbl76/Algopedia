package Java.EssentialAlgorithms.Chapter9_Recursion.BackTracking;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class KnightsTour1 {

    /*
        CONS:
            - this solution suffers from following long paths before determining it is a wild goose chase.

     */

    //static int dimension = ExecUtils.getRandom(8, 5);
    static int dimension = 7;
    static int squares = dimension * dimension;
    static List<List<Integer>> move = new ArrayList<>();
    static List<Integer> legalRows = Arrays.asList(-2, -2, -1, 1, 2, 2, 1, -1);
    static List<Integer> legalCols = Arrays.asList(-1, 1, 2, 2, 1, -1, -2, -2);

    public static void main(String[] args) {
        setupBoard();

        System.out.println("Dimension: " + dimension);
        long start = System.nanoTime();
        if (solve(0, 0, 0, 0)) {
            printBoard();
        } else {
            System.out.println("No solution");
        }
        long end = System.nanoTime();

        System.out.println(dimension + " x " + dimension + " board [" + squares + "]");
        System.out.println("Time to Solve: " + TimeUnit.NANOSECONDS.toMillis(end - start));

    }

    public static void setupBoard() {
        for (int i = 0; i < dimension; i++) {
            List<Integer> integers = new ArrayList<>();
            for (int j = 0; j < dimension; j++) {
                integers.add(0);
            }
            move.add(integers);
        }
    }

    public static void printBoard() {
        StringBuilder pretty = new StringBuilder();
        move.forEach(integers -> {
            integers.forEach(integer -> {
                pretty.append(String.format("[%3d]", integer)).append(" ");
            });
            pretty.append('\n');
        });
        System.out.println(pretty);
    }

    private static boolean solve(int row, int col, int move_counter, int attempts) {
        attempts++;
        move_counter++;
        move.get(row).set(col, move_counter);
        System.out.println("Move: " + move_counter);

        // easy use case. If we've hit all of the squares, we're good
        if (move_counter == squares)
            return true;

        // walk through legal moves
        for (int i = 0; i < legalRows.size(); i++) {
            int x = row + legalRows.get(i);
            int y = col + legalCols.get(i);

            /* '
                Make sure we don't fall off the edge and that the move hasn't
                already been visited.
             */
            if ((x >= 0 && x < dimension) &&
                    (y >= 0 && y < dimension) &&
                    (move.get(x).get(y) == 0)) {
                if (solve(x, y, move_counter, attempts))
                    return true;
            }
        }

        // BackTrack step
        System.out.println("\tDAMMIT!!!!");
        move.get(row).set(col, 0);
        return false;
    }

}
