package Java.EssentialAlgorithms.Chapter10_Trees.Expressions;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class ExpressionsApp3 {

    static ExpressionsNode root;
    static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) {


        /*
            sqrt( x * y / a * b)
         */
        root = new ExpressionsNode(Operators.SquareRoot);

        // now we are inside the sqrt, so let's work on division
        root.setLeft(new ExpressionsNode(Operators.Divide));

        // set each "side" to times.
        root.getLeft().setLeft(new ExpressionsNode(Operators.Times));
        root.getLeft().setRight(new ExpressionsNode(Operators.Times));

        // Add in the values.
        IntStream.rangeClosed(1,4).forEach(value -> list.add(ExecUtils.getRandom(24, 1)));
        root.getLeft().getLeft().setLeft(new ExpressionsNode(String.valueOf(list.get(0))));
        root.getLeft().getLeft().setRight(new ExpressionsNode(String.valueOf(list.get(1))));
        root.getLeft().getRight().setLeft(new ExpressionsNode(String.valueOf(list.get(2))));
        root.getLeft().getRight().setRight(new ExpressionsNode(String.valueOf(list.get(3))));

        System.out.println("Calculating: Sqrt(" + list.get(0) + " * " + list.get(1)
                + " / " + list.get(2) + " * " + list.get(3) + ")");
        System.out.println("Results: " + root.evaluate());
        System.out.println("Check  : " +  (
                Math.sqrt(((double)list.get(0) * list.get(1)) / ((double)list.get(2) * list.get(3))))
                );


        System.out.println();
    }

}
