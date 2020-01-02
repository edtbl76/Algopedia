package Java.EssentialAlgorithms.Chapter10_Trees.Expressions;

import Java.EssentialAlgorithms.Utils.ExecUtils;

public class ExpressionsApp1 {

    static ExpressionsNode root;
    static ExpressionsNode left;
    static ExpressionsNode right;

    static int oper1, oper2, oper3, oper4;

    public static void main(String[] args) {



        /*
            Addition Expression
         */
        createOperands(false);
        System.out.println("Adding " + oper1 + " and " + oper2);
        root = new ExpressionsNode(Operators.Plus);
        root.setLeft(new ExpressionsNode(String.valueOf(oper1)));
        root.setRight(new ExpressionsNode(String.valueOf(oper2)));
        System.out.println("Result: " +  root.evaluate());
        System.out.println("Check: " + (double)(oper1 + oper2) + "\n");

        /*
            Nested Expression 1
         */
        createOperands(true);
        System.out.println("Adding The result of ( " + oper1 + " / " + oper2 + " ) and ( " + oper3 + " / " + oper4 + " )");

        setOperators(Operators.Plus, Operators.Divide, Operators.Divide);
        setOperands();
        finalizeExpressionTree();

        System.out.println("Result: " + root.evaluate());
        System.out.println("Check1: " + (left.evaluate() + right.evaluate()));
        System.out.println("Check2: " + ((double)oper1 / oper2 + ((double)oper3 / oper4)) + "\n");

        /*
            Nested Expression 2
         */
        createOperands(true);
        setOperands();
        System.out.println("Subtracting The result of ( " + oper1 + " * " + oper2 + " ) and ( " + oper3 + " * " + oper4 + " )");

        setOperators(Operators.Minus, Operators.Times, Operators.Times);
        setOperands();
        finalizeExpressionTree();

        System.out.println("Result: " + root.evaluate());
        System.out.println("Check1: " + (left.evaluate() - right.evaluate()));
        System.out.println("Check2: " + ((double)oper1 * oper2 - ((double)oper3 * oper4)) + "\n");

    }

    public static void setOperators(Operators op1, Operators op2, Operators op3) {
        root = new ExpressionsNode(op1);
        left = new ExpressionsNode(op2);
        right = new ExpressionsNode(op3);
    }

    public static void createOperands(boolean four) {
        if (four) {
            oper3 = ExecUtils.getRandom(25, 1);
            oper4 = ExecUtils.getRandom(25, 1);
        }
        oper1 = ExecUtils.getRandom(25, 1);
        oper2 = ExecUtils.getRandom(25, 1);
    }

    public static void setOperands() {
        left.setLeft(new ExpressionsNode(String.valueOf(oper1)));
        left.setRight(new ExpressionsNode(String.valueOf(oper2)));
        right.setLeft(new ExpressionsNode(String.valueOf(oper3)));
        right.setRight(new ExpressionsNode(String.valueOf(oper4)));
    }

    public static void finalizeExpressionTree() {
        root.setLeft(left);
        root.setRight(right);
    }


}
