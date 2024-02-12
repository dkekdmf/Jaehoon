import java.util.Scanner;

public class BOJ2884 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int M = sc.nextInt();

        if(M>45){
            M-=45;
        }
        else{
            H-=1;
            M+=15;
            if(H<0){
                H = 23;
            }

        }
        System.out.println(H+" "+M);

    }
}
