package Java.EssentialAlgorithms.Chapter10_Trees.Expressions;

enum Operators {
    Literal,
    Plus,
    Minus,
    Times,
    Divide,
    Negate,
    SquareRoot,
    Factorial,
    Sine,
    Squared,
}

public class ExpressionsNode {

    private Operators operator;
    private ExpressionsNode left;
    private ExpressionsNode right;
    private String literal;

    ExpressionsNode() {}

    ExpressionsNode(Operators operator) {
        this();
        this.operator = operator;
    }

    ExpressionsNode(String text) {
        this();
        this.operator = Operators.Literal;
        this.literal = text;
    }

    /*
        BizLoj
     */
    public double evaluate() {

        switch(this.operator) {
            case Literal:
                return Double.parseDouble(literal);
            case Plus:
                return left.evaluate() + right.evaluate();
            case Minus:
                return left.evaluate() - right.evaluate();
            case Times:
                return left.evaluate() * right.evaluate();
            case Divide:
                return  left.evaluate() / right.evaluate();
            case Negate:
                return -left.evaluate();
            case SquareRoot:
                return Math.sqrt(left.evaluate());
            case Factorial:
                return factorial(left.evaluate());
            case Sine:
                return Math.sin(Math.PI / 180.0 * left.evaluate());
            case Squared:
                double leftvalue = left.evaluate();
                return Math.pow(leftvalue, 2);
            default:
                throw new ArithmeticException("Unknown operator " +  this.operator.toString());
        }
    }

    public static double factorial(double number)  {
        double result = 1;
        for (int i = 2; i <= number; i++) {
            result *= i;
        }
        return result;

    }

    /*
        Getters & Setters
     */

    public Operators getOperator() {
        return operator;
    }

    public void setOperator(Operators operator) {
        this.operator = operator;
    }

    public ExpressionsNode getLeft() {
        return left;
    }

    public void setLeft(ExpressionsNode left) {
        this.left = left;
    }

    public ExpressionsNode getRight() {
        return right;
    }

    public void setRight(ExpressionsNode right) {
        this.right = right;
    }

    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
}
