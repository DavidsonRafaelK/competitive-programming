class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diff = {}
        heap = []

        for i in nums:
            if i in diff:
                diff[i] += 1
            else:
                diff[i] = 1
        
        for index, value in sorted(diff.items(), key=lambda item: item[1], reverse=True):
            heap.append(index)
        
        return heap[:k]