import java.util.Arrays;
import java.util.Scanner;

public class BOJ1546 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        double sum=0;
        Double[] arr = new Double[N];
        for(int i=0;i<arr.length;i++)
            arr[i]= sc.nextDouble();
        for (int i = 0; i < N; i++) {

            Arrays.sort(arr);


            sum += (arr[i] / arr[arr.length - 1] * 100);

        }
            System.out.println(sum/arr.length);
        }


        }



