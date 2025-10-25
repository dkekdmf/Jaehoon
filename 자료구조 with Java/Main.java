import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

//TIP 코드를 <b>실행</b>하려면 <shortcut actionId="Run"/>을(를) 누르거나
// 에디터 여백에 있는 <icon src="AllIcons.Actions.Execute"/> 아이콘을 클릭하세요.
public class Main {

    public static int fibonacci(int data){

        if (data<=1)
            return data;
        else
            return fibonacci(data-1) + fibonacci(data-2);

    };

    //타뷸레이션 상향식
    public static int dpBottomUp(int data){
        int []dp = new int[data+1];
        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 1;
        for (int i = 3; i <data+1 ; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[data];

    }
    //메모이제이션 하향식

    public static  int dpTopDown(int data){
       int []memo = new int[data+1];

       if (data <=1) return data;
       if (memo[data]!=0){
           return memo[data];
        }
       memo[data] = dpTopDown(data-1) + dpTopDown(data-2);
       return memo[data];


    }

    public static void main(String[] args) {

//        0 1 1 2 3 5 7 12 19

        System.out.println(fibonacci(7));
        System.out.println(dpTopDown(7));
        System.out.println(dpBottomUp(7));
        //TIP 캐럿을 강조 표시된 텍스트에 놓고 <shortcut actionId="ShowIntentionActions"/>을(를) 누르면
        // IntelliJ IDEA이(가) 수정을 제안하는 것을 확인할 수 있습니다.

        }
    }
