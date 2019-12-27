package Java.EssentialAlgorithms.Chapter10_Trees.AnimalGame;

import java.util.Scanner;

public class AnimalGameExample {

    public static Animal root;
    public static void main(String[] args) {
        root = new Animal("Is it a mammal?");
        root.setYes(new Animal("dog"));
        root.setNo(new Animal("fish"));

        Animal node = root;
        Scanner scanner = new Scanner(System.in);
        gameLoop(scanner, node);
        scanner.close();

    }

    private static void gameLoop(Scanner scan, Animal node) {
        while (true) {
            if (node.getYes() == null) {
                processLeaf(scan, node);

                // play it again loop.
                boolean playMore = handleInput(scan, "Play Again? ");
                if (playMore)
                    gameLoop(scan, root);
                else
                    return;
            }
            node = (handleInput(scan, node.getQuestion())) ? node.getYes() : node.getNo();
        }
    }

    private static boolean handleInput(Scanner scan, String question) {
        System.out.println(question);

        String answer = null;
        answer = scan.nextLine();

        if (answer.equalsIgnoreCase("yes"))
            return true;
        else if (answer.equalsIgnoreCase("no"))
            return false;
        else
            return handleInput(scan, question);
    }

    private static void processLeaf(Scanner scan, Animal leaf) {
        boolean result = handleInput(scan, "Is your animal " + leaf.name() + "?");
        if (result) {
            System.out.println("You Win!");
        } else {
            getSmarter(scan, leaf);
        }
    }

    private static void getSmarter(Scanner scan, Animal node) {
        System.out.println("What was your animal?");
        String animal_name = scan.nextLine().toLowerCase();
        Animal animal = new Animal(animal_name);

        System.out.println(
                "What question could I ask to differentiate between " + node.name() + " and " + animal.name() + "?");

        String animal_question = scan.nextLine();
        String old_animal = node.getQuestion();
        node.setQuestion(animal_question);
        boolean result = handleInput(scan, "Is the answer to this question true for " + animal.name() + "?");
        if (result) {
            node.setYes(new Animal(animal_name));
            node.setNo(new Animal(old_animal));
        } else {
            node.setYes(new Animal(old_animal));
            node.setNo(new Animal(animal_name));
        }
        }
}
