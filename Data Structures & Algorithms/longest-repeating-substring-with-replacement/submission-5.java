class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character,Integer> map=new HashMap<>();
        int len=s.length();
        int count;
        int maxFreq=0;
        int left=0;
        int max=0;
        for(int i=0;i<len;i++){ 
            count=map.getOrDefault(s.charAt(i),0);
            count++;
            map.put(s.charAt(i),count);
            for(Map.Entry<Character,Integer> entry: map.entrySet()){
                if (entry.getValue() > maxFreq) {
                maxFreq = entry.getValue();
               }
            }
            int wl=i-left+1;  //windowlength
            if(wl-maxFreq <= k){
                if(wl>max){
                    max=wl;
                }
                continue;
            }
            if(wl-maxFreq>k){
                
                count=map.get(s.charAt(left));
                map.replace(s.charAt(left),count-1);
                left++;
            }
        } 
        return max;      
    }
}
