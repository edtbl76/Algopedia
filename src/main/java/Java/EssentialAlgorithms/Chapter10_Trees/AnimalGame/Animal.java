package Java.EssentialAlgorithms.Chapter10_Trees.AnimalGame;


import java.util.LinkedList;

public class Animal {

    private String question;
    private Animal yes;
    private Animal no;

    Animal() {}

    public Animal(String question) {
        this.question = question;
    }


    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }

    public Animal getYes() {
        return yes;
    }

    public void setYes(Animal yes) {
        this.yes = yes;
    }

    public Animal getNo() {
        return no;
    }

    public void setNo(Animal no) {
        this.no = no;
    }

    public String name() {
        String vowels = "aeiou";
        /*
            Convert input to lower case and get the first character.
            - convert the char back to a string, because string.contains() doesn't support a single character
            -  (which is fucking stupid)
         */
        if (vowels.contains(String.valueOf(question.toLowerCase().charAt(0)))) {
            return "an " + question;
        }
        return "a " +  question;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        LinkedList<Animal> kids = new LinkedList<>();
        kids.addFirst(this);

        while(kids.size() > 0) {
            Animal node = kids.removeLast();
            sb.append(" ").append(node.question);

            if (node.getYes() != null)
                kids.addFirst(node.getYes());
            if (node.getNo() != null)
                kids.addFirst(node.getNo());
        }
        return String.valueOf(sb).stripLeading();
    }
}
