class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}

        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0)+1

        list_values = list(freq_dict.values())
        list_values.sort(reverse = True)
        
        return [key for key in freq_dict if freq_dict[key] in list_values[:k]]