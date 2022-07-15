n,m,k=map(int,input().split())
data=list(map(int,input().split()))
result=0
data.sort()
first=data[n-1]
second=data[n-2]
if first==second:
  result=first*m
  print(33)
else:
  result=first*(m//k)*k+second*(m%k)
    
print(result)