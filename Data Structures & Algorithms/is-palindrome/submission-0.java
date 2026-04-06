class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        char[] arr=s.toCharArray();
        int i=0;
        int j=arr.length-1;
        while(i<j){ 

            if(arr[i]!=arr[j] && Character.toUpperCase(arr[i])!=Character.toUpperCase(arr[j])){ 
                System.out.println("comparison failed for arr[i]="+arr[i]+" and arr[j]="+arr[j]);
                return false;
            }
            else{
                i++;
                j--;
            }
        }
        return true;
    }
}
