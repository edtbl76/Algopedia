package Java.EssentialAlgorithms.Chapter7_Searching;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.List;

public class RecursiveInterpolationSearch {

    public static void main(String[] args) {
        int target = ExecUtils.getRandom(20, 1);
        List<Integer> list = ExecUtils.populateCollection(20, 8, true);
        System.out.println("Initial: " + list);

        int result = findIndex(list, 0, list.size() - 1, target, 0);
        ExecUtils.findIndexPrinter(target, result);

    }

    private static int findIndex(List<Integer> list, int min, int max, int target, int steps) {

        steps++;
        System.out.print("\tSteps: " + steps);
        System.out.println("\tSearching on ("+ min + "," + max  +")");

        /*
         * If min and max are equal... then the only possible option left is to be min.
         */
        if(list.get(min).equals(list.get(max))) {
            if (list.get(min) == target)
                return min;
            return -1;
        }

        // Get divider
        int divider = min + (max - min) * (target - list.get(min)) / (list.get(max) - list.get(min));
        System.out.println("\t\tDivider: " + divider);

        // If divider is insane.. bail out.
        if ((divider < min) || (divider > max))
            return -1;

        // Which way do we look
        if (list.get(divider) < target)
            min = divider + 1;
        else if (list.get(divider) > target)
            max = divider - 1;
        else
            return divider;

        // We can't just return, we have to make sure min is <= max
        if (min <= max)
            return findIndex(list, min, max, target, steps);

        return -1;
    }
}
