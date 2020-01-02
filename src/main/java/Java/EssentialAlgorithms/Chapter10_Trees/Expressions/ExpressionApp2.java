package Java.EssentialAlgorithms.Chapter10_Trees.Expressions;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class ExpressionApp2 {

    static ExpressionsNode root;
    static ExpressionsNode left;
    static ExpressionsNode right;
    static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) {

        IntStream.rangeClosed(1, 6).forEach(value -> list.add(ExecUtils.getRandom(24, 1)));

        root = new ExpressionsNode(Operators.Plus);
        left = new ExpressionsNode(Operators.Divide);
        left.setLeft(new ExpressionsNode(String.valueOf(list.get(0))));
        left.setRight(new ExpressionsNode(String.valueOf(list.get(1))));
        root.setLeft(left);

        root.setRight(new ExpressionsNode(Operators.Plus));
        // Left is just a placeholder! Don't get confused :) We've already assigned the value of  left to root.left
        left = new ExpressionsNode(Operators.Divide);
        left.setLeft(new ExpressionsNode(String.valueOf(list.get(2))));
        left.setRight(new ExpressionsNode(String.valueOf(list.get(3))));
        root.getRight().setLeft(left);

        right = new ExpressionsNode(Operators.Divide);
        right.setLeft(new ExpressionsNode(String.valueOf(list.get(4))));
        right.setRight(new ExpressionsNode(String.valueOf(list.get(5))));
        root.getRight().setRight(right);

        System.out.println("Calculating: (" + list.get(0) + " / " + list.get(1)
                + " + " + list.get(2) + " / " + list.get(3)
                + " + " + list.get(4) + " / " + list.get(5) + ")");
        System.out.println("Results: " + root.evaluate());
        System.out.println("Check  : " +
                ((double)list.get(0) / list.get(1)
                        + (double)list.get(2) / list.get(3)
                        + (double)list.get(4) / list.get(5)));

    }

}
