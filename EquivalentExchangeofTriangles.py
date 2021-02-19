'''
# Problem Code:LEQEX



#CODE :

# cook your dish here
import numpy as np
tests = int(input())
for _ in range(tests):
   n = int(input())
   nums = [int(j)-1 for j in input().split()]
   
   pow_2 = [1 for _ in range(30)]
   for i in range(1,30):
      pow_2[i] = 2 * pow_2[i-1]
   
   colors = [-1 for _ in range(30)]
   seen = dict()
   seen[0] = -1
   max_height = 0
   num = 0
   for i in range(n):
      colors[nums[i]] = -colors[nums[i]]
      num += pow_2[nums[i]] * colors[nums[i]]
      for j in range(30):
         new_num = num + pow_2[j] * (-colors[j])
         if new_num in seen:
            max_height = max(max_height,(i-seen[new_num])//2)
      if num not in seen:
         seen[num] = i
   print(max_height)
