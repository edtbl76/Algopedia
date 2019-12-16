package Java.EssentialAlgorithms.Chapter9_Recursion.BackTracking;

import Java.EssentialAlgorithms.Utils.ExecUtils;

public class EightQueens1 {

    static int placed = 0;

    public static void main(String[] args) {
        int queens = ExecUtils.getRandom(16, 4);
        System.out.println(queens + " queens");

        // set up board.
        int[][] board = new int[queens][queens];
        for(int i = 0; i < queens; i++)
            for(int j = 0; j < queens; j++)
                board[i][j] = 0;

        // No solution
        if (!solve(board, 0, queens))
            System.out.println("No Solution");
        else
            display(board, queens);

    }

    private static void display(int[][] board, int queens) {
        for(int row = 0; row < queens; row++) {
            for(int col = 0; col < queens; col++) {
                System.out.print(" " + board[row][col] + " ");
            }
            System.out.println();
        }
    }

    private static boolean check(int[][] board, int row, int col, int queens) {

        int x;
        int y;

        // Check this row (left side)
        for (x = 0; x < col; x++)
            if (board[row][x] == 1) {
                System.out.println("\t\tSame Row!");
                return false;
            }

        // check upper diagonal
        for (x = row, y = col; x >= 0 && y >=0; x--,y--)
            if (board[x][y] == 1) {
                System.out.println("\t\tUpper Diag!");
                return false;
            }

        // check lower diag
        for (x = row, y = col; y >= 0 && x < queens; x++, y--)
            if (board[x][y] == 1) {
                System.out.println("\t\tLower Diag!");
                return false;
            }

        return true;
    }

    private static boolean solve(int[][] board, int col, int queens) {

        // If all queens are placed, we're done
        if (col >= queens)
            return true;

        for (int row = 0; row < queens; row++) {

            if (check(board, row, col, queens)) {
                System.out.println("\tTrying (" + row + "," + col + ")");
                // If it is safe, put queen in square
                board[row][col] = 1;
                placed++;
                System.out.println("\t\tPlaced " + placed + " queens");

                // If we have a solution, we're done
                if (solve(board, col + 1, queens))
                    return true;

                // Backtrack if we haven't solved.
                board[row][col] = 0;
                System.out.println("\t\tShit! Backtracking.");
                placed--;
            }
        }

        // If queen can't be placed in any row in this column, bail out.
        return false;
    }
}


/*
    ALGORITHM STEPS

    1.) Start in leftmost column
    2.) if all queens placed return true
    3.) try all rows in current columne
        - (a) if queen can be placed in this row safely
            - mark row, col as part of solution and recursively check if placing queen leads to solution

        - if placing queen at row, col leads to solution, return true
        - if placing queen fails, unmark the spot
            - backtrack to (a) to try other rows
    4.) if all rows have been tried and nothing worked, return false to trigger backchecking
 */