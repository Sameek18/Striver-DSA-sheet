#using counting sort TC:O(n^2)

def Countsort(nums,n):
    count0,count1,count2=0,0,0
    for i in range(0,n):
        if nums[i]==0:
            count0+=1
        elif nums[i]==1:
            count1+=1
        elif nums[i]==2:
            count2+=1

    for i in range(0,count1):
        nums[i]=0

    for i in range(count1,count0+count1):
        nums[i]=1

    for i in range(count0+count1,n):
        nums[i]=2

    return(nums)


#Using Dutch national flag algo O(n)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #we want all 0s before low , all 1s before mid and all 2s starting from high
        #initialize three pointers
        low=0
        mid=0
        high=len(nums)-1      
        while(mid<=high):
            if nums[mid]==0:
                nums[low],nums[mid]=nums[mid],nums[low]   #since mid is 0, we will swap it with low
                low+=1
                mid+=1
            elif nums[mid]==1:    
                mid+=1
            else:
                 nums[high],nums[mid]=nums[mid],nums[high]  #since mid is 2 we will swap it with high
                 high-=1
                 mid+=1
                    
        return nums
