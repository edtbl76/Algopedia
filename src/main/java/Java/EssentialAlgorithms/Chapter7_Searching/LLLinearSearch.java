package Java.EssentialAlgorithms.Chapter7_Searching;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.List;

public class LLLinearSearch {

    public static void main(String[] args) {
        List<Integer> list = ExecUtils.populateCollection(30, 10);
        System.out.println("Initial LL: " + list);

        int target = ExecUtils.getRandom(30, 1);
        int result = findIndex(list, target, 0);

        if (result > 0) {
            System.out.println("Found " + target + " at index " + result);
        } else {
            System.out.println("No " + target + "s here!");
        }
    }

    private static int findIndex(List<Integer> list, int target, int steps) {
        int index = 0;
        System.out.print("\tSteps: ");
        for (Integer integer : list) {

            steps++;
            System.out.print(steps + " ");

            if (integer == target) {
                System.out.print("\n");
                return index;
            }
            index++;
        }
        System.out.print("\n");
        return -1;


    }
}
