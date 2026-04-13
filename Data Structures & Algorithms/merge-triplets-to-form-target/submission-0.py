class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # To track if we've found a valid value for target[0], target[1], and target[2]
        found_x = found_y = found_z = False
        
        target_x, target_y, target_z = target
        
        for a, b, c in triplets:
            # Step 1: Check if the triplet is "safe" 
            # (none of its elements exceed the target values)
            if a <= target_x and b <= target_y and c <= target_z:
                
                # Step 2: Check if this safe triplet provides any of the target values
                if a == target_x:
                    found_x = True
                if b == target_y:
                    found_y = True
                if c == target_z:
                    found_z = True
            
            # Optimization: If we found all three, we can stop early
            if found_x and found_y and found_z:
                return True
                
        return False