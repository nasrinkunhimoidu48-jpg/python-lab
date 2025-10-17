list1=[1,2,3,4,5,6]
list2=[2,4,6,8]
a=len(list1)
print("the length of first list is:",a)
b=len(list2)
print("the length of second list is:",b)
if(a==b):
    print("length are same")
else:
    print("length are not same")

c=sum(list1)
print("sum=",c)
d=sum(list2)
print("sum=",d)
if(c==d):
    print("the sum of list1 and list2 are equal")
else:
    print("the sum of list1 and list2 are not equal")

for i in list1:
    for j in list2:
        if (i==j):
            print(i)
