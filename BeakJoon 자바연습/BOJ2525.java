import java.util.Scanner;

public class BOJ2525 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int S = (A*60+B+C)%1440;//하루를 초과할수있기ㄸ문에

        int H = S/60;
        int M = S%60;
        if(H==24)
            H=0;




        System.out.println(H+" "+M);
    }
}
