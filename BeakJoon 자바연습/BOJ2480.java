import java.util.Scanner;

public class BOJ2480 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int S = sc.nextInt();

        if(N==M&&M==S&&N==S){
            System.out.println(10000+(N*1000));
        }
        else if(N==M){
            System.out.println(1000+(N*100));
        }
        else if(M==S)
            System.out.println(1000+(S*100));
        else if(N==S)
            System.out.println(1000+(N*100));
        else
            System.out.println(Math.max(N,Math.max(S,M))*100);
    }
}
