from collections import Counter
from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:

    # Count frequency of each element - O(n)
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]
    
    # Place elements in buckets based on their frequency - O(n)
    for num, freq in frequency.items():
        buckets[freq].append(num)
    
    # Collect elements from highest frequency buckets - O(n)
    result = []
    for freq in range(n, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result 