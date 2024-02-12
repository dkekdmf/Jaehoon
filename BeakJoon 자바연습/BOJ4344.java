import java.util.Scanner;

public class BOJ4344 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for(int t=0;t<T;t++) {
            int n = sc.nextInt();
            int []arr = new int[n];
            int sum = 0;

            for (int j = 0; j < n; j++) {
                arr[j] = sc.nextInt();
                sum+=arr[j];
            }
            double avg = sum / n;
            double count = 0;

            for (int i = 0; i < arr.length; i++) {
                if (arr[i] > avg)
                    count++;
            }
            System.out.printf("%.3f%%\n",(count/n)*100);
        }
    }
}
