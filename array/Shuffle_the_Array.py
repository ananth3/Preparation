class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr1 = nums[:n]
        arr2 = nums[n:]
        j = 0
        for i in range(1,len(nums),2):
            arr1.insert(i,arr2[j])

            j+=1
        return arr1
