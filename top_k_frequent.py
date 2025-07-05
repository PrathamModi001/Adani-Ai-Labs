from collections import Counter
from typing import List

# BASIC BUCKET SORT ALGORITHM

def top_k_frequent(nums: List[int], k: int) -> List[int]:

    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    
    for num, freq in frequency.items():
        buckets[freq].append(num)
    
    result = []
    for freq in range(n, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result 


print(top_k_frequent([1,1,1,2,2,3], 2))