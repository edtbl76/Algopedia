package Java.EssentialAlgorithms.Chapter9_Recursion.BasicRecursion;

import Java.EssentialAlgorithms.Utils.ExecUtils;

public class TowerOfHanoi {

    static int counter = 0;

    public static void main(String[] args) {
        int disks = ExecUtils.getRandom(20, 3);
        System.out.println("TowersOfHanoi with " + disks + " disks");
        System.out.println(towersOfHanoi("LEFT", "MIDDLE", "RIGHT", disks));
        System.out.println("Recursions: " + counter);
    }

    private static String towersOfHanoi(String from, String to, String other, int disks) {

        counter++;

        StringBuilder result = new StringBuilder();

        /*
            Move the top N - 1 disks from "from" to "other"
         */
        if (disks > 1)
            result.append(towersOfHanoi(from, other, to, disks - 1));

        // move last disk from "from" to "to"
        if (disks > 1) {
            result.append(" ");
        }
        result.append(from).append("->").append(to).append("\n");

        // recursively move top n - 1 from "other" to "to"
        if (disks > 1)
            result.append(" ").append(towersOfHanoi(other, to, from, disks - 1));

        return String.valueOf(result);
    }
}

/**
    Sequence of Events: (3 disks)

    Result = ""

    L M R 3         From Main
    - (IF1)
        L R M 2     From IF1
        - (IF1)
            L M R 1
            - APPEND: "Left->Middle", RETURN
        - APPEND: " "   (IF2)
        - APPEND: "Left->Right"
        - APPEND: " "   (IF3)
        - (IF3)
            M R L 1
            - APPEND: "Middle->Right", RETURN
        RETURN
    - APPEND: " " (IF2)
    - APPEND: "Left->Middle"
    - APPEND: " " (IF3)
    - (IF3)
        R M L 2     From IF3
        - (IF1)
            R L M 1
            - APPEND: "Right->Left", RETURN
        - APPEND " " (IF2)
        - APPEND "Right->Middle"
        - APPEND " " (IF3)
        - (IF3)
            - L M R 1
                - APPEND "Left->Middle", RETURN
        RETURN
    RETURN

 */
