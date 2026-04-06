class Solution {

    public String encode(List<String> strs) { 
        StringBuilder sb =new StringBuilder();

        for(String s:strs){
            sb.append(s);
            sb.append(";");   
        }
        return sb.toString();

    }

    public List<String> decode(String str) {
       StringBuilder sb=new StringBuilder();
       List<String> list=new ArrayList<>();
       for(char c:str.toCharArray()){
          if(c!=';'){
            sb.append(c);
          }
          else{
            list.add(sb.toString());
            sb=new StringBuilder();
          }
       }
       return list;
    }
}
