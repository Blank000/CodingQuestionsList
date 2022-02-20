class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = {}
        for i in range(len(nums)):
            self.dic[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for k,v in self.dic.items():
            if k in vec.dic:
                res += vec.dic[k]*v
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)