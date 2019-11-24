package Java.EssentialAlgorithms.Chapter3_LinkedLists;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

import static Java.EssentialAlgorithms.Chapter3_LinkedLists.CircularLinkedListImpl.Node;

public class ListReversalExample {

    public static void main(String[] args) {
        Node<String> head = builder(true);
        Node<String> temp = head;

        System.out.println("=== LOOP ===");
        for(int i = 1;i <= 10; i++) {
            System.out.println("value: " + temp  +  " next: " + temp.getNext());
            temp = temp.getNext();
        }
        System.out.println("LOOP=" + hasLoop(head));

        head = builder(false);
        temp = head;
        System.out.println("=== NO LOOP ===");
        for(int i = 1;i <= 10; i++) {
            System.out.println("value: " + temp  +  " next: " + temp.getNext());
            temp = temp.getNext();
        }
        System.out.println("LOOP=" + hasLoop(head));
    }

    private static  Node<String> reverseLinks(Node<String> sentinel) {
        Node<String> previous = null;
        Node<String> current = sentinel;
        while(current != null) {
            Node<String> next = current.getNext();
            current.setNext(previous);

            previous = current;
            current = next;
        }
        return previous;
    }

    private static boolean hasLoop(Node<String> node) {
        // empty lists have no loops
        if (node.getNext() == null)
            return false;

        // loop through, reversing links
        Node<String> newHead = reverseLinks(node);
        reverseLinks(newHead);
        if (node == newHead)
            return true;
        return false;
    }

    private static void printList(Node<String> node) {
        Node<String> temp = node;
        for(int i = 1; i < 10; i++) {
            System.out.print(temp.getNext() + " ");
            temp = temp.getNext();
        }
        System.out.println();
    }

    private static Node<String> builder(boolean loop) {
        // Create Some Nodes
        Node<String> head = new Node<>(null);
        Node<String> nodeA = new Node<>("A");
        Node<String> nodeB = new Node<>("B");
        Node<String> nodeC = new Node<>("C");
        Node<String> nodeD = new Node<>("D");
        Node<String> nodeE = new Node<>("E");
        Node<String> nodeF = new Node<>("F");
        Node<String> nodeG = new Node<>("G");
        Node<String> nodeH = new Node<>("H");
        Node<String> nodeI = new Node<>("I");

        // Set Their Links
        head.setNext(nodeA);
        nodeA.setNext(nodeB);
        nodeB.setNext(nodeC);
        nodeC.setNext(nodeD);
        nodeD.setNext(nodeE);
        nodeE.setNext(nodeF);
        nodeF.setNext(nodeG);
        nodeG.setNext(nodeH);
        nodeH.setNext(nodeI);
        if(loop)
            nodeI.setNext(nodeD);
        else
            nodeI.setNext(null);

        return head;
    }
}
