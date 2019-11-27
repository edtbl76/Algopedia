package Java.EssentialAlgorithms.Chapter4_Arrays.Matrices;

public class AddSparseArrays {

    public static void main(String[] args) {
        SparseArray<Integer> array1 = new SparseArray<>(0);
        array1.set(1, 1, 101);
        array1.set(-1, -1, -101);
        array1.set(3, 3, 303);
        array1.set(2, 4, 204);
        array1.set(4, 1, 401);
        System.out.println("Array1: " + array1);

        SparseArray<Integer> array2 = new SparseArray<>(0);
        array2.set(1,0,100);
        array2.set(3,3,303);
        array2.set(1,4,104);
        array2.set(4,1,401);
        array2.set(10,10,1010);
        array2.set(11,11,1111);
        System.out.println("Array2: " + array2);

        SparseArray<Integer> array3 = array1.add(array2);
        System.out.println("Array3: " + array3);

    }
}
