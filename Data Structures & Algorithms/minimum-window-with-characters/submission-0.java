class Solution {
    public String minWindow(String s, String t) {
        HashMap<Character,Integer> map=new HashMap<>();
        for(int i=0;i<t.length();i++){
                map.put(t.charAt(i), map.getOrDefault(t.charAt(i), 0)+1);
        }
        int left=0;
        int right=0;
        boolean flag=false;  // flag to decide if the we have found atleast the first letter from t
        String output=""; 
        HashMap<Character,Integer> copy=new HashMap<>(map);
        while(right<s.length()){
            if(!copy.containsKey(s.charAt(right))){
                if(!flag){
                    left++;
                }
            }
            else {
                if(!flag){
                    flag=true;
                } 
                if(copy.get(s.charAt(right))>1){
                    copy.put(s.charAt(right), copy.get(s.charAt(right))-1);
                }  
                else{
                    copy.remove(s.charAt(right));
                }
                 
            }
            right++;
            if(copy.isEmpty()){  
                //System.out.println("The code did reach here for string ");
                //System.out.println(s.substring(left,right));
                int len=s.substring(left,right).length();
                if(output.isEmpty()){
                    output=s.substring(left,right);
                }

                if( len<output.length()){ 
                    System.out.println("this if case matched");
                    output=s.substring(left,right);
                }
                copy=new HashMap<>(map);
                left++;
                right=left;
            }             
            
        }
        return output;
    }
}
