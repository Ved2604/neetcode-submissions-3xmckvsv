class Solution {
    public List<List<String>> groupAnagrams(String[] strs) { 
        HashMap<String ,List<String>> map=new HashMap<>();
        for(String s:strs){
            char[] arr=s.toCharArray();
            Arrays.sort(arr);
            String sorteds=new String(arr);
            map.putIfAbsent(sorteds, new ArrayList<>());
            map.get(sorteds).add(s);
        }
        return new ArrayList<>(map.values());
        
    }
}
