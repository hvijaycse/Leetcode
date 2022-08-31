import java.util.HashMap;

class Solution {

    static int max(int a, int b){
        return ( a > b ) ? a : b;
    }

    public int lengthOfLongestSubstring(String s) {

        HashMap<Character, Integer> map = new HashMap<Character, Integer>();

        int LongestSubstring = 0;
        int lastIndex = -1;


        for(int index = 0; index < s.length(); index++){
            
            if(map.containsKey(s.charAt(index))){
                lastIndex = max(lastIndex, map.get(s.charAt(index)));
            }

            LongestSubstring = max(LongestSubstring, index - lastIndex);

            map.put(s.charAt(index), index);

        }

        return LongestSubstring;
        
    }
}

class LongestSubstring{
    public static void main(String[] args) {
        
        System.out.println("Hello world");
    }
}