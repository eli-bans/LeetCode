class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = collections.defaultdict(int)
        bucket = [[]for i in range(len(nums)+1)]

        #find every number and the number of times it appears
        for n in nums:
            hashMap[n] +=1 #+ hashMap.get(n,0)
        
        #find the numbers in the map and add them to the bucket, 
        #according to their frequency 
        for freq in hashMap:
            bucket[hashMap[freq]].append(freq)

        #find the top k frequent elements 
        res = []
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
            if len(res) == k:
                return res   

        