package Java.DataStructures.Lists.Exec;

import java.util.ArrayList;
import java.util.List;

public class MergeSortedArrayList {

    public static void main(String[] args) {
        List<Integer> odds = new ArrayList<>();
        List<Integer> evens = new ArrayList<>();
        List<Integer> merged = new ArrayList<>();

        for(int i = 1; i <= 10; i +=2) {
            odds.add(i);
            evens.add(i + 1);
        }

        merge(odds, evens, merged);

        System.out.println("Odds: " + odds);
        System.out.println("Evens: " + evens);
        System.out.println("Merged: " + merged);

    }

    private static void merge(List<Integer> listOne, List<Integer> listTwo, List<Integer> mergeList) {
        int ctr1 = 0, ctr2 = 0;

        /*
        logic to ensure merge list is inserted from lowest to highest
            - the condition for the while loop will iterate through the length of both parameter lists
            - inside if the value in list one is <= value of list two,  post incr (this gets the value and then increments
            it after we are done. its a twofer)
         */
        while(ctr1 < listOne.size() && ctr2 < listTwo.size()) {
            if (listOne.get(ctr1) <= listTwo.get(ctr2)) {
                mergeList.add(listOne.get(ctr1++));
            } else {
                mergeList.add(listTwo.get(ctr2++));
            }
        }

        while(ctr1 < listOne.size())
            mergeList.add(listOne.get(ctr1++));

        while(ctr2 < listTwo.size())
            mergeList.add(listTwo.get(ctr2++));


    }
}
