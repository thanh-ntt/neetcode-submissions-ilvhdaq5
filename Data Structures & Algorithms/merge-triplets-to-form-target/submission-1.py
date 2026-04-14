class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_triplets = [t for t in triplets if (t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2])]
        first = any(t[0] == target[0] for t in valid_triplets)
        second = any(t[1] == target[1] for t in valid_triplets)
        third = any(t[2] == target[2] for t in valid_triplets)
        return first and second and third