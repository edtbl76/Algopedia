package Java.EssentialAlgorithms.Chapter10_Trees.SortedTree;

import Java.EssentialAlgorithms.Utils.ExecUtils;

public class SortedTreeExample {

    public static void main(String[] args) {

        int size = ExecUtils.getRandom(10, 1);
        System.out.println("Creating a Sorted Tree with " + size + " nodes");

        BinaryNode node = new BinaryNode();
        for(int i = 0; i < size; i++) {
            node.add(ExecUtils.getRandom(100, 1));
        }
        System.out.println(node.breadthFirst());
    }

}
