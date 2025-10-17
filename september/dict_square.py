print("dictionary square")
n=int(input("enter a number"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
if n<=15:
    print(d)
