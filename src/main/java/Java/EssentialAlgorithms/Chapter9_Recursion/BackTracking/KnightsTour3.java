package Java.EssentialAlgorithms.Chapter9_Recursion.BackTracking;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.awt.*;
import java.util.*;
import java.util.List;
import java.util.concurrent.TimeUnit;


/*
    Perf drop
    7 ~ 11 seconds
    8 ~
 */
public class KnightsTour3 {
    //static int dimension = ExecUtils.getRandom(8, 5);
    static int dimension = 6;

    static List<List<Integer>> move = new ArrayList<>();
    static List<List<List<Point>>> legalMoves = new ArrayList<>();

    static final List<Integer> legalRows = Arrays.asList(-2, -2, -1, 1, 2, 2, 1, -1);
    static final List<Integer> legalCols = Arrays.asList(-1, 1, 2, 2, 1, -1, -2, -2);

    public static void main(String[] args) {

        System.out.println("Dimensions: " + dimension);
        setupBoard();
        long start = System.nanoTime();
        if (solve(0, 0, 0))
            printBoard();
        else
            System.out.println("No Solution");

        long end = System.nanoTime();
        System.out.println("Dimensions: " + dimension);
        System.out.println("TTSL: " + TimeUnit.NANOSECONDS.toMillis(end - start));
    }

    static void setupBoard() {

        for(int row = 0; row < dimension; row++) {
            List<Integer> integers = new ArrayList<>();
            for(int col = 0; col < dimension; col++) {
                integers.add(0);
            }
            move.add(integers);
        }

        setupLegalMovesTable();
    }

    static void printBoard() {
        StringBuilder pretty = new StringBuilder();
        move.forEach(integers -> {
            integers.forEach(integer -> pretty.append(String.format("%3d", integer)).append(" "));
            pretty.append('\n');
        });
        System.out.println(pretty);
    }

    static void setupLegalMovesTable() {

        for (int row = 0; row < dimension; row++) {
            List<List<Point>> list = new ArrayList<>();
            for (int col = 0; col < dimension; col++) {
                List<Point> points = new ArrayList<>();
                for (int i = 0; i < 8; i++) {
                    int x = row + legalRows.get(i);
                    int y = col + legalCols.get(i);
                    if (x >=0 && x < dimension && y >= 0 && y < dimension)
                        points.add(new Point(x, y));
                }
                list.add(points);
            }
            legalMoves.add(list);
        }

        /*
            This optimization orders the "legal moves" list on a per column basis, so each time we
            perform a Comparison, we're going to look for the shortest solutions first.

            THis decreases the chance of our algorithm going down "long long" paths of
            failure.
         */
        System.out.println("Entering Sort");
        //legalMoves.forEach(lists -> lists.sort(Comparator.comparingInt(List::size)));
        System.out.println("Exiting Sort");

       /* legalMoves.forEach(lists -> {
            System.out.print("Lists");
            System.out.println(lists.size());
            lists.forEach(points -> {
                System.out.print("Points");
                System.out.println(points.size());
            });

        });*/
    }

    static int getMoves(int row, int col) {
        return (int) legalMoves.get(row).get(col)
                .stream()
                .filter(point -> move.get(point.x).get(point.y) == 0).count();
    }

    static boolean boundsCheck(int x, int y) {
        return (x >= 0 && x < dimension && y >= 0 && y < dimension && move.get(x).get(y) == 0);
    }

    static boolean solve(int row, int col, int moves) {
        moves++;
        move.get(row).set(col, moves);

        if (moves == dimension * dimension)
            return true;

        // scan though next moves from current position
        List<Point> moves_list = new ArrayList<>();
        legalMoves.get(row).get(col).forEach(point -> {
            if (move.get(point.x).get(point.y) == 0)
                moves_list.add(point);
        });

        while (moves_list.size() > 0) {
            Point best = moves_list.get(0);
            int best_counter = getMoves(best.x, best.y);
            for (Point current_move : moves_list) {
                int test_counter = getMoves(current_move.x, current_move.y);
                if (best_counter < test_counter) {
                    best_counter = test_counter;
                    best = current_move;
                }
            }
            moves_list.remove(best);

            if (boundsCheck(best.x, best.y)) {
                if (solve(best.x, best.y, moves))
                    return true;
            }
        }

        // Backtracking
        move.get(row).set(col, 0);
        return false;
    }
}
