# cook your dish here
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    x=a//b + a%b
    print(x)
    
