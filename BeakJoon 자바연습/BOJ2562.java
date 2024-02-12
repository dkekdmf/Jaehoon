import java.util.Scanner;

public class BOJ2562 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr= new int[10];
        int max = -1000001;
        int point =0;
        for(int i=0;i<9;i++) {
            arr[i] = sc.nextInt();
        }
        for(int i=0;i<9;i++) {
            if (arr[i]>max) {
                max = arr[i];
                point = i+1;
            }

        }
        System.out.println(max+"\n"+point);
    }
}
