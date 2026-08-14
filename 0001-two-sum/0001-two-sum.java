import java.util.HashMap;
class Solution {
    public int[] twoSum(int[] nums, int target) {
       HashMap <Integer, Integer> map = new HashMap<>();
       int n=0;
       for(int i=0;i<nums.length;i++){
        n=target-nums[i];
        if(map.containsKey(n)){
            return new int[]{map.get(n),i};
        }
        map.put(nums[i],i);

       }
       return new int[]{};
}
}