
class Solution {
    public String longestPalindrome(String s) {

        int longestLength, left, right;
        longestLength = 0;
        left = 0;
        right = 0;

        for(int index=0; index < s.length(); index++){

            int tempLeft = index;
            int tempRight = index;

            while(tempRight< s.length() && s.charAt(tempRight) == s.charAt(index)){
                tempRight += 1;
            }

            tempRight -= 1;

            while(tempLeft >= 0 && tempRight < s.length()  && s.charAt(tempLeft) == s.charAt(tempRight)){
                tempLeft -= 1;
                tempRight += 1;
            }

            tempLeft += 1;
            tempRight -= 1;

            if ( (tempRight - tempLeft + 1) > longestLength ){
                longestLength = tempRight - tempLeft + 1;
                left = tempLeft;
                right = tempRight;
            }
        }
        

        return s.substring(left, right+1);
    }
}

class longestPalindrome{
    public static void main(String[] args) {
        
        System.out.println("Hello world");
    }
}