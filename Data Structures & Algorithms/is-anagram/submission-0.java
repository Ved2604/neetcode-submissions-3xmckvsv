class Solution {
    public boolean isAnagram(String s, String t) {
      char[] arr1=s.toCharArray();
      char[] arr2=t.toCharArray();
      if(arr1.length!=arr2.length){
        return false;
      }
      HashMap<Character, Integer> map=new HashMap<>();
      for(int i=0;i<arr1.length; i++){
        if(map.containsKey(arr1[i])){
            int count=map.get(arr1[i]);
            count++;
            map.replace(arr1[i],count);
        }
        else map.put(arr1[i],1);
      }
      for(int j=0;j<arr2.length;j++){
        if(map.containsKey(arr2[j]) && map.get(arr2[j])>0){
            int count=map.get(arr2[j]);
            count--;
            if(count==0){
                map.remove(arr2[j]);
                continue;
            }
            map.replace(arr2[j],count);
        }
        else return false;
      }
      if(map.size()==0){
        return true;
      }
      else return false;


    }
}
