import java.util.Random;

public class ArrayMethod {
    // 배열 5가지 메소드
    public static void change(int arr[],int idx,int val){
        arr[idx] = val;
    }
    public static boolean erase(int arr[],int arrcount,int idx){
        if(idx>=arrcount)
            return false;
        for(int i = idx;i<arrcount;i++)
            arr[i] = arr[i+1];
        return true; //O(N)

    }
    public static boolean insert(int arr[],int arrcount,int idx,int val){
        if(idx>arrcount || arrcount>=arr.length)
            return false;
        for(int i = arrcount; i>idx; i--)
            arr[i] = arr[i-1];
            arr[idx] = val;
            return true;
    }
    public static boolean append(int arr[], int arrcount,int val){
        if(arrcount==arr.length){
            return false;
        }
        arr[arrcount] = val;
        return true;
    }
    public static  int get(int []arr,int idx){
        return arr[idx];
    }
    // 랜덤함수 배열에 넣기
    public static void main(String[] args) {
        int []arr = new int[10];
        Random rand = new Random();

        for(int i = 0; i<arr.length;i++){
            arr[i] = rand.nextInt(5);

        }
        for(int i=0;i<arr.length;i++){
            System.out.println(arr[i]);

        }



         double randomvalue = Math.random();
         int intvalue = (int)(randomvalue*100)+1;

        for(int i=0 ; i<10;i++){
            arr[i]+=i;
        }


        for (int i=0; i< arr.length;i++){
            System.out.println(arr[i]);
        }

    }
}
