import java.util.Arrays;

class Main {
    public static void main(String[] args) {
        int[] arr = { 0, 1, 0, 3, 12 };
        // Calling moveZerosToEnd();
        moveZerosToEnd(arr);
        System.out.println(Arrays.toString(arr));
    }

    // Two Pointer Approach:
    private static void moveZerosToEnd(int[] arr) {
        int si = 0, ei = 0;
        while (ei < arr.length) {
            while (ei < arr.length && arr[ei] == 0)
                ei++;
            // Now, the ei stands in a non-zero element:
            while (si < arr.length && arr[si] != 0)
                si++;
            // Now the si is stands in a zero element

            // Checking for Valid Swapping:
            if (si < arr.length && ei < arr.length
            && arr[si] == 0 && arr[ei] != 0){
                // Now, Swap them:
                int temp = arr[si];
                arr[si] = arr[ei];
                arr[ei] = temp;
            }
        }
    }
}