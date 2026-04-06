class Solution {
    public int trap(int[] height) { 
        int leftmax;
        int rightmax;
        int[] water=new int[height.length];
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
            water[i]=Math.min(leftmax,rightmax)-height[i];
            
        }
        for(int l=0;l<water.length;l++){
            sum=sum+water[l];
        }
        return sum;
    }
}
