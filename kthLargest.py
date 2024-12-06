# Solved on Leetcode: Yes
# Any Problems: Tried to create a Heap from scratch.

# Time: O(nlogk) 
# space: O(k)
#Min Heap
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq  = []
        for num in nums:
            heapq.heappush(pq,num)          # push element to heap, auto-heapify
            # print(pq)
            if len(pq)>k:
                heapq.heappop(pq)           # pop n-1th element 
        return heapq.heappop(pq)            # last pop gives kth element

# [3]
# [2, 3]
# [1, 3, 2]
# [2, 3, 5]
# [3, 5, 6]
# [4, 6, 5]
 
 #time:(n+k*log(n))
#  Space : O(n)
# Max heap with filled pq
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = [-i for i in nums]
        # print(pq)                             # [-3, -2, -1, -5, -6, -4]
        heapq.heapify(pq)
        # print(pq)                             # [-6, -5, -4, -3, -2, -1]
        for i in range(k-1):  
            heapq.heappop(pq)
        # print(pq)                             # [-5, -3, -4, -1, -2]
        return -1 * heapq.heappop(pq)
    