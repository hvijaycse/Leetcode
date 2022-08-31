import java.util.HashMap;


class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        
        HashMap<Integer, Integer> map = new HashMap<>();

        int[] ans = new int[2];

        for(int index=0; index < nums.length; index++){

            int targetkey = target - nums[index];

            if (map.containsKey(targetkey)){
                ans[0] = map.get(targetkey);
                ans[1] = index;
                break;
            }

            map.put(nums[index], index);
        } 

        // System.out.print(map);

        return ans;
        
    }
}

class TwoSum{

    public static void main(String[] args) {
        System.out.println("This is my first Solution");
    }
}