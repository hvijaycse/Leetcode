class Solution {
    public int reverse(int x) {

        boolean isNegative = x < 0;
        int answer = 0;

        x = Math.abs(x);

        
        while (x > 0) {

            long overflow = (long) answer;

            if((overflow*10) + (x % 10) > Integer.MAX_VALUE){
                answer = 0;
                break;
            }
            answer *= 10;
            answer += x % 10;
            x /= 10;
        }


        return (isNegative) ? -answer: answer;
        
    }
}

class reverseInteger{
    public static void main(String[] args) {
        System.out.println("Hello world");
    }
}