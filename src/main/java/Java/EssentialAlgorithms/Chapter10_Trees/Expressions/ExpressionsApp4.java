package Java.EssentialAlgorithms.Chapter10_Trees.Expressions;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class ExpressionsApp4 {

    static ExpressionsNode root;
    static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) {

        /*
            5! / ((5 - 3)! * 3!)
         */
        IntStream.rangeClosed(1, 4).forEach(value -> list.add(ExecUtils.getRandom(10, 1)));
        root = new ExpressionsNode(Operators.Divide);

        // Handle left branch
        root.setLeft(new ExpressionsNode(Operators.Factorial));
        root.getLeft().setLeft(new ExpressionsNode(String.valueOf(list.get(0))));

        // Handle Right branch
        root.setRight(new ExpressionsNode(Operators.Times));
        root.getRight().setLeft(new ExpressionsNode(Operators.Factorial));
        root.getRight().setRight(new ExpressionsNode(Operators.Factorial));

        // Right Right
        root.getRight().getRight().setLeft(new ExpressionsNode(String.valueOf(list.get(3))));

        // Right Left
        root.getRight().getLeft().setLeft(new ExpressionsNode(Operators.Minus));
        root.getRight().getLeft().getLeft().setLeft(new ExpressionsNode(String.valueOf(list.get(1))));
        root.getRight().getLeft().getLeft().setRight(new ExpressionsNode(String.valueOf(list.get(2))));

        System.out.println("Calculating: "
                + list.get(0) + "! / ((" + list.get(1) + " - " + list.get(2) + ")! * " + list.get(3) + "!");
        System.out.println("Result: " + root.evaluate());
        System.out.println("Check: " + (
                ExpressionsNode.factorial(list.get(0)) / (ExpressionsNode.factorial(list.get(1) - list.get(2)) * ExpressionsNode.factorial(list.get(3)))
                ));
    }
}
