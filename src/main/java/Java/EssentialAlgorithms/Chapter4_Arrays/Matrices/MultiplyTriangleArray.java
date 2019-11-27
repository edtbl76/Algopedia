package Java.EssentialAlgorithms.Chapter4_Arrays.Matrices;

public class MultiplyTriangleArray {

    private static final int ROWS = 3;

    public static void main(String[] args) {

        TriangleArray array1 = new TriangleArray(ROWS);
        array1.set(0,0,1);
        array1.set(1,0,2);
        array1.set(1,1,3);
        array1.set(2,0,4);
        array1.set(2,1,5);
        array1.set(2,2,6);
        System.out.println("Array1: " + array1);

        TriangleArray array2 = new TriangleArray(ROWS);
        array2.set(0,0,10);
        array2.set(1,0,20);
        array2.set(1,1,30);
        array2.set(2,0,40);
        array2.set(2,1,50);
        array2.set(2,2,60);
        System.out.println("Array2: " + array2);

        TriangleArray array3 = array1.timesFull(array2);
        System.out.println("Array3: " + array3);

        TriangleArray array4  = array1.times(array2);
        System.out.println("Array4: " + array4);

    }
}
