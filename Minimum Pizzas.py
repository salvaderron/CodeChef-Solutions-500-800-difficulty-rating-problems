import math
# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    slice_need=a*b
    print(math.ceil(slice_need/4))
