package Java.EssentialAlgorithms.Chapter10_Trees.Expressions;


import Java.EssentialAlgorithms.Utils.ExecUtils;

public class ExpressionsApp5 {

    static ExpressionsNode root;
    static int oper1;

    public static void main(String[] args) {

        oper1 = ExecUtils.getRandom(360, 1);

        /*
            // Sine(45)^2
         */
        root = new ExpressionsNode(Operators.Squared);
        root.setLeft(new ExpressionsNode(Operators.Sine));
        root.getLeft().setLeft(new ExpressionsNode(String.valueOf(oper1)));
        System.out.println("Calculate: sin(" + oper1 + ")^" + 2);
        System.out.println("Result: " + root.evaluate());
        System.out.println("Check : " + Math.pow(Math.sin(oper1 * Math.PI / 180), 2));
    }
}

