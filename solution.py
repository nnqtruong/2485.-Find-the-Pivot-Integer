class Solution(object):
    def pivotInteger(self, n):
        total_sum = n * (n + 1) // 2  # Calculate the sum of all numbers from 1 to n
        sumfront = 0
        
        for i in range(1, n + 1):
            sumfront += i  # Add the current number to the sumfront
            
            # Check if sumfront equals the required pivot condition
            if sumfront == total_sum - sumfront + i:
                return i
        
        return -1  # Return -1 if no such pivot exists
