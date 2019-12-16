package Java.EssentialAlgorithms.Chapter9_Recursion.BackTracking;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class EightQueens2 {

    static List<List<Boolean>> board = new ArrayList<>();
    static List<List<Integer>> attacks = new ArrayList<>();

    static int dimension = ExecUtils.getRandom(16, 4);

    public static void main(String[] args) {


        System.out.println("Queens: " + dimension);
        long start = System.nanoTime();

        setupBoard(dimension);
        if (solve(0, 0))
            displayBoard();
        else
            System.out.println("No Solution");

        long end = System.nanoTime();
        System.out.println("Queens: " + dimension);
        System.out.println("Time To Solve: " + TimeUnit.NANOSECONDS.toMillis(end - start));
    }

    public static void setupBoard(int dimension) {
        for (int i = 0; i < dimension; i++) {
            List<Boolean> booleans = new ArrayList<>();
            List<Integer> integers = new ArrayList<>();

            for (int j = 0; j < dimension; j++) {
                booleans.add(false);
                integers.add(0);
            }
            board.add(booleans);
            attacks.add(integers);
        }
    }

    public static void displayBoard() {
        StringBuilder pretty = new StringBuilder();
        board.forEach(booleans -> {
            booleans.forEach(aBoolean -> {
                if(aBoolean)
                    pretty.append('X');
                else
                    pretty.append('-');
                pretty.append(' ');
            });
            pretty.append('\n');
        });
        System.out.println(pretty);
    }

    private static boolean solve(int placed, int attempts) {
        // if we've placed all queens, yay!
        if(placed == dimension)
            return true;

        for(int row = 0; row < dimension; row++) {
            for(int col = 0; col < dimension; col++) {
                /*
                    This is kind of cool. Instead of checking per square, we mark the number of attacks
                    so the safety check for placement is simpler on the main solve() method.

                    (Although it is slow as shit past 12 X 12
                 */
                if (!board.get(row).get(col) && attacks.get(row).get(col) == 0) {
                    // if its ok, place queen
                    attempts++;
                    System.out.println("\tAttempt #" + attempts);

                    /* set board position to true, and we set attacks at from that position
                       - by setting the attacks we've more or less eager loaded all of the
                       states that block future placement
                    */
                    board.get(row).set(col,true);
                    setAttacks(row, col, 1);

                    // try next
                    if (solve(placed + 1, attempts))
                        return true;

                    // if we get this far, we hit a dead end.
                    System.out.println("\tShit! Backtrack!");
                    setAttacks(row, col, -1);
                    board.get(row).set(col, false);
                }
            }
        }

        return false;
    }

    public static void setAttacks(int x, int y, int value) {

        //mark row (one-liner is a bit too ugly, I broke it up for readabiliity)
        for (int row = 0; row < dimension; row++) {
            List<Integer> attack_row = attacks.get(row);
            attack_row.set(y, attack_row.get(y) + value);
        }

        // mark col
        for (int col = 0; col < dimension; col++) {
            List<Integer> attack_col = attacks.get(x);
            attack_col.set(col, attack_col.get(col) + value);
        }

        // upper left/low right diag
        int min_diag1 = -Math.min(x, y);
        int max_diag1 = Math.min(dimension - x - 1, dimension - y - 1);
        for(int i = min_diag1; i <= max_diag1; i++) {
            List<Integer> list = attacks.get(x + i);
            list.set(y + i, list.get(y + i) + value);
        }

        // lower left/upper right diag
        int min_diag2 = -Math.min(x, dimension - y - 1);
        int max_diag2 = Math.min(dimension - x - 1, y);
        for (int i = min_diag2; i <= max_diag2; i++) {
            List<Integer> list = attacks.get(x + i);
            list.set(y - i, list.get(y - i) + value);
        }
    }
}
