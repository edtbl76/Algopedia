package Java.EssentialAlgorithms.Chapter9_Recursion.BackTracking;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class KnightsTour2 {
    //static int dimension = ExecUtils.getRandom(16, 5);
    static int dimension = 7;
    static List<List<Integer>> board = new ArrayList<>();
    static List<List<List<Point>>> legalMoves = new ArrayList<>();


    static final List<Integer> rowList = Arrays.asList(-2, -2, -1, 1, 2, 2, 1, -1);
    static final List<Integer> colList = Arrays.asList(-1, 1, 2, 2, 1, -1, -2, -2);

    public static void main(String[] args) {

        System.out.println("Dimensions: " + dimension);

        setupBoard();
        long start = System.nanoTime();

        if (solve(0,0,0))
            printBoard();
        else
            System.out.println("No Solution");

        long end = System.nanoTime();
        System.out.println("Dimensions: " + dimension);
        System.out.println("TTS: " + TimeUnit.NANOSECONDS.toMillis(end - start));
    }

    static boolean boundsCheck(int x, int y) {
        return (x >= 0 && x < dimension && y >= 0 && y < dimension && board.get(x).get(y) == 0);
    }

    static void setLegalMovesTable() {

        for (int row = 0; row < dimension; row++) {
            List<List<Point>> list = new ArrayList<>();

            for(int col = 0; col < dimension; col++) {
                List<Point> points = new ArrayList<>();
                for(int i = 0; i < 8; i++) {

                    int x = row + rowList.get(i);
                    int y = col + colList.get(i);
                    if (x >= 0 && x < dimension && y >=0 && y < dimension)
                        points.add(new Point(x, y));
                }
                list.add(points);
            }
            legalMoves.add(list);
        }

    }

    static int getMoves(int row, int col) {
        return (int) legalMoves.get(row).get(col)
                .stream()
                .filter(point -> board.get(point.x).get(point.y) == 0).count();
    }

    static boolean solve(int row, int col, int moves) {
        moves++;
        board.get(row).set(col, moves);

        if (moves == dimension * dimension)
            return true;

        // scan though next moves from current position
        List<Point> moves_list = new ArrayList<>();
        legalMoves.get(row).get(col).forEach(point -> {
            if (board.get(point.x).get(point.y) == 0)
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
        board.get(row).set(col, 0);
        return false;
    }

    static void setupBoard() {
        for (int row = 0; row < dimension; row++) {
            List<Integer> list = new ArrayList<>();
            for (int col = 0; col < dimension; col++) {
                list.add(0);
            }
            board.add(list);
        }

        setLegalMovesTable();
    }

    static void printBoard() {
        StringBuilder pretty = new StringBuilder();
        board.forEach(integers -> {
            integers.forEach(integer -> pretty.append(String.format("%3d", integer)).append(" "));
            pretty.append('\n');
        });
        System.out.println(pretty);
    }
}
