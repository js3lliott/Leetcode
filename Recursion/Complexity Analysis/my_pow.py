# Implement pow(x, n), which calculates x raised to the power n (x^n)

# Input: 2.00000, 10
# Output: 1024.00000

# Input: 2.00000, -2
# Output:0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x * x, n/2)