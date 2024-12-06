# Min heap - k Merge
# Time : O(N log k) N for iterating over Nodes and logK for heappush 7 ms 
# Space: O(k) heap size 
# Issues: TypeError comparison in heappush
# Leetcode: Yes
import heapq
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i,li in enumerate(lists): 
            if li:                          # add all head nodes
                heapq.heappush(pq, (li.val,i,li))       #added all elements in ListNode + i for enumerate "1,2,3,4"// if val is eq, check i , check li

        dummy = ListNode(-1)                # dummy head
        curr = dummy                        

        while pq:                           # initialize a Min Heap
            _,_,currMin = heapq.heappop(pq) # error://'<' not supported between instances of 'ListNode' and 'ListNode'//
            curr.next = currMin 
            curr = curr.next
            if currMin.next:
                heapq.heappush(pq,(currMin.next.val,id(currMin.next),currMin.next)) # unquie values for all newer nodes "140347050743696"
                # print(id(currMin.next))                                            # value,unique_id,node
        return dummy.next

# 2 lists- k merge SUPERSLOW 1148 ms
# Time: O(N^2 log k)
# Space : O(1) no extra space 
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        merged = None
        
        for li in lists:
            merged = self.merge(merged,li)
        return merged

    def merge(self,l1,l2):
        dummy = ListNode(-1)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        if l1:
            curr.next = l1

        if l2:
            curr.next = l2

        return dummy.next