package Java.EssentialAlgorithms.Chapter7_Searching;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.List;

public class RecursiveLinearSearch {

    public static void main(String[] args) {
        int target = ExecUtils.getRandom(20, 1);

        // Unsorted
        List<Integer> list = ExecUtils.populateCollection(20, 10);
        System.out.println("Initial: " + list);

        int result = findIndex(list, 0, target, 0, false);
        ExecUtils.findIndexPrinter(target, result);

        // Sorted version for fun
        List<Integer> listSorted = ExecUtils.populateCollection(20, 10, true);
        System.out.println("Sorted: " + list);

        int resultBetter = findIndex(listSorted, 0, target, 0, true);
        ExecUtils.findIndexPrinter(target, resultBetter);

    }

    private static int findIndex(List<Integer> list, int index, int target, int steps, boolean sorted) {

        steps++;
        System.out.println("\tSteps: " + steps + " Index: " + index);

        if(index == list.size())
            return -1;

        if(list.get(index) == target)
            return index;

        /*
            If we sorted the input list, we could optimize this solution by
            checking if list[index] > target (or < then depending on how it is sorted).

            I added a little conditional short circuit and updated it above to demonstrate.
         */
        if (sorted)
            if(list.get(index)> target)
                return -1;


        return findIndex(list, index + 1, target, steps, sorted);
    }
}
