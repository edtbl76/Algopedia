package Java.EssentialAlgorithms.Utils;

public class ExecUtils {
    public static int getRandom(int max, int min) {
        return (int)(Math.random() * ((max - min) + 1) + min);
    }
}
