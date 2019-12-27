package Java.EssentialAlgorithms.Chapter10_Trees.ThreadedTrees;

import Java.EssentialAlgorithms.Utils.ExecUtils;

import java.util.ArrayList;
import java.util.List;

public class ThreadedTreeExample {

    public static void main(String[] args) {

        int size = ExecUtils.getRandom(16, 2);
        System.out.println("Creating a threaded tree with " + size + " nodes");

        ThreadedNode node = new ThreadedNode();
        for(int i = 0; i < size; i++) {
            node.addNode(ExecUtils.getRandom(20, 1));
        }

        System.out.println(print(getForwardTraversal(node)));
        System.out.println(print(getBackwardTraversal(node)));

    }

    private static List<ThreadedNode> getForwardTraversal(ThreadedNode node)  {
        List<ThreadedNode> traversal = new ArrayList<>();

        // switch to determine if traversal is by branch or by thread
        boolean branch = true;

        // while we've got a node to process.. process it!
        while (node != null) {

            // if by branch.. go to the left
            if (branch) {

                while (node.getLeftChild() != null)
                    node = node.getLeftChild();
            }
            // add it to list
            traversal.add(node);

            if (node.getRightChild() == null) {
                // If branch is empty use thread.
                node = node.getRightThread();
                branch = false;
            } else {
                // else... use branch
                node = node.getRightChild();
                branch = true;
            }

        }
        // return what we've got.
        return traversal;
    }

    private static List<ThreadedNode> getBackwardTraversal(ThreadedNode node) {
        List<ThreadedNode> traversal = new ArrayList<>();
        boolean branch = true;

        while(node != null) {
            if (branch) {
                while (node.getRightChild() != null)
                    node = node.getRightChild();
            }
            traversal.add(node);

            if (node.getLeftChild() == null) {
                node = node.getLeftThread();
                branch = false;
            } else {
                node = node.getLeftChild() ;
                branch = true;
            }
        }
        return traversal;
    }

    public static String print(List<ThreadedNode> node) {
        StringBuilder sb = new StringBuilder();

        node.forEach(threadedNode -> {
            sb.append(" ").append(threadedNode.getValue());
        });

        return String.valueOf(sb).stripLeading();
    }
}
