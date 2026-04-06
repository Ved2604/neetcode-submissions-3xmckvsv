class Solution {
    public int trap(int[] height) { 
        int leftmax;
        int rightmax;
        int sum=0;
        for(int i=0;i<height.length;i++){
            leftmax=height[i];
            rightmax=height[i];
            for(int j=i;j>=0;j--){
                if(height[j]>leftmax){
                    leftmax=height[j];
                }
            }
            for(int k=i;k<height.length;k++){
                if(height[k]>rightmax){
                    rightmax=height[k];
                }
            }
            sum=sum+Math.min(leftmax,rightmax)-height[i];
            
        }
        return sum;
    }
}
