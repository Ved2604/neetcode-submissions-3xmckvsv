class Solution {
    public boolean checkInclusion(String s1, String s2) {  
        if(s2.length()<s1.length()){
            return false;
        }
        char[] arr=s1.toCharArray();
        //List<Character> list=new ArrayList<>();
        HashMap<Character,Integer> map=new HashMap<>();
        for(char c:arr){
            map.put(c, map.getOrDefault(c, 0)+1);
        }
        int left=0;
        int k=s1.length();
        int right=left+k-1;
        boolean bool=false;
        while(right<s2.length()){ 
            //List<Character> lc=new ArrayList<>(list);    //list copy 
            HashMap<Character,Integer> cmap=new HashMap<>(map);   //map copy
            //System.out.println("Left="+left+" Right="+right+ " cmap="+cmap);


            for(int i=left;i<=right;i++){  
                 //System.out.println("Inside for loop for left="+left+ " right="+right+" i="+i+" and char inside the window="+s2.charAt(i));
                if(!cmap.containsKey(s2.charAt(i))){
                    break;
                }
                else{
                    if(cmap.get(s2.charAt(i))>1){
                        cmap.put(s2.charAt(i), cmap.get(s2.charAt(i))-1);
                    }
                    else {
                        cmap.remove(s2.charAt(i));
                        if(cmap.isEmpty()){
                        return true;
                    }
                    }
                    
                }

            }
            left++;
            right++;
        }
        return bool;
        
    }
}
