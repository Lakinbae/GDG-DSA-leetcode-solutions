a,b,m=map(int, input("enter a,b,m").split())
#result=pow(a,b,m)
result=1
for _ in range(b):
    result = (result*a)%m
print(result)