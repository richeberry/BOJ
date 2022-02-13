# 2775 _ 부녀회장이 될테야


for _ in range(int(input())): # t 
  k = int(input()) # floor
  n = int(input()) # room
  floor = [i for i in range(1,n+1)] # make rooms number 1 to n

  for _ in range(k): # from 2nd to k floor
      for i in range(1,n): # from 2 to n room ('room 1' is always 1) 
          floor[i] += floor[i-1] # under floor's last room peole -> next floor's 
  print(floor[-1]) # last index = sum of peple live in