#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Mia Stein

'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
'''
 

def climb_stairs_o2n(n: int) -> int:
 
        if n == 0 or n == 1:
            return 1
        return climb_stairs_o2n(n - 1) + climb_stairs_o2n(n - 2)
 

def climb_stairs_memoization(n: int) -> int:
 
    memo = {}    

    def helper(n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = helper(n - 1, memo) + helper(n - 2, memo)
        return memo[n]
 
   return helper(n, memo)

    
def climb_stairs_optimized(n: int) -> int:
 
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
 
        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
         
        return curr


def climb_stairs_tabulation(n: int) -> int:
 
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
         
        return dp[n]
