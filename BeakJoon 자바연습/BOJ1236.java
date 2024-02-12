import java.util.Scanner;

public class BOJ1236 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        char [][] arr = new char[N][M];
        for(int i=0;i<N;i++)
            arr[i] = sc.next().toCharArray();
        int existRowCount = 0;
        for(int i=0;i<N;i++){
            boolean exist= false;
            for(int j=0;j<M;j++){
                if(arr[i][j]=='X') {
                    exist = true;
                    break;
                }
            }
            if(exist) existRowCount++;
        }
        int existColCount =0;
        for(int j=0;j<M;j++){
            boolean exist = false;
            for(int i=0;i<N;i++){
                if(arr[i][j]=='X') {
                    exist = true;
                    break;
                }
            }
            if(exist)existColCount++;
        }
        int needRowCount = N-existRowCount;
        int needColCount =M-existColCount;

        System.out.println(Math.max(needRowCount,needColCount));

    }
}
