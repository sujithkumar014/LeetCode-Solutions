int removeElement(int* nums, int numsSize, int val) {
    for(int i=0;i<numsSize;i++){
        if(nums[i]==val){
            for(int j=i+1;j<numsSize;j++){
                if(nums[i]!=nums[j]){
                    int temp=nums[i];
                    nums[i]=nums[j];
                    nums[j]=temp;
                    break;
                }
            }
        }
    }
    int k=0;
    for(int i=0;i<numsSize;i++){
        if(nums[i]!=val){
            k++;
        }
    }

    return k;
}