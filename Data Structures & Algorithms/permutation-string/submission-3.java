class Solution {
    public boolean checkInclusion(String s1, String s2) {  
        if(s2.length()<s1.length()){
            return false;
        }
        char[] arr=s1.toCharArray();
        List<Character> list=new ArrayList<>();
        for(char c:arr){
            list.add(c);
        }
        int left=0;
        int k=s1.length();
        int right=left+k-1;
        boolean bool=false;
        while(right<s2.length()){ 
            List<Character> lc=new ArrayList<>(list);    //list copy 

            for(int i=left;i<=right;i++){  

                if(!lc.contains(s2.charAt(i))){
                    break;
                }
                else{
                    lc.remove((Character) s2.charAt(i)); 
                    if(lc.isEmpty()){
                        return true;
                    }
                }

            }
            left++;
            right++;
        }
        return bool;
        
    }
}
