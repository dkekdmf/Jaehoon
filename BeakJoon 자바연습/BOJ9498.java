import java.util.Scanner;

public class BOJ9498 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N= sc.nextInt();
        if (N>=90&&N<=100)
            System.out.println('A');
        else if(N>=80&&N<90)
            System.out.println('B');
        else if(N>=70 &&N<80)
            System.out.println('C');
        else if(N>=60&&N<70)
            System.out.println('D');
        else
            System.out.println('F');


    }
}
