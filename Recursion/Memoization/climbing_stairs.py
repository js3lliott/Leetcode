# You are climbing a stair case. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct
# ways can you climb to the top?
# Note: Given n will be a positive integer


class Solution:
    def climbingStairs(self, n):

        cache = {}

        def climbing_stairs(n):

            if n in cache:
                return cache[n]

            elif n <= 3:
                result = n

            else:
                result = climbing_stairs(n - 1) + climbing_stairs(n - 2)

            cache[n] = result
            return result

        return climbing_stairs(n)