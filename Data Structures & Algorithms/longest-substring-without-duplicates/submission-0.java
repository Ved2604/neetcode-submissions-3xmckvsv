class Solution {
    public int lengthOfLongestSubstring(String s) { 
        if(s.length()==0){
            return 0;
        }
        HashSet<Character> set=new HashSet<>();
        char[] arr=s.toCharArray();
        int left=0;
        set.add(arr[0]);
        int max=1;
        for(int i=1;i<arr.length;i++){
            
            while (set.contains(s.charAt(i))) {
                set.remove(arr[left]);
                left++;
            }
                set.add(arr[i]);
                max=Math.max(i-left+1,max);
             
        }
        return max;
    }
}
