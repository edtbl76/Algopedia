package Java.EssentialAlgorithms.Chapter7_Searching;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.List;

public class RecursiveBinarySearch {


    public static void main(String[] args) {
        List<Integer> list= ExecUtils.populateCollection(20,10, true);
        System.out.println("Initial: " + list);

        int target = ExecUtils.getRandom(20, 1);
        int result = findIndex(list, 0, list.size() - 1, target, 0);

        ExecUtils.findIndexPrinter(target, result);

    }

    private static int findIndex(List<Integer> list, int min, int max, int target, int steps) {

        // Iter printer.
        steps++;
        System.out.print("\tSteps: " + steps);
        System.out.println("\tSearching: " + "(" + min + "," + max+ ")");

        int mid = (min + max) / 2;

        // Hole in one?
        if (target == list.get(mid)) {
            return mid;
        }

        // Left or Correct?
        if (target < list.get(mid)) {
            System.out.println("\tLeft!");
            max = mid - 1;
        } else {
            System.out.println("\tRight!");
            min = mid + 1;
        }

        if (min <= max) {
            return findIndex(list, min, max, target, steps);
        }

        return -1;
    }

}
