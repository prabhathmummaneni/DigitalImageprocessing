#1
def generatenumbers(num):
    a=[]
    for i in range(0,num+1):
        a.append(i)
    return a
print(generatenumbers(10))
#2
def generatenumbersinrange(a,b,c):
    d=[]
    while (a<=b):
        d.append(a)
        a+=c
    return d
print(generatenumbersinrange(1,11,2))
#3
def addnumbers(num):
    a=0
    for i in range(0,num+1):
        a+=(i)
    return a
print(addnumbers(10))
#4
def sort_list(a):
    a.sort()
    return a
a=[2,4,3,1,7,0,9,10,0]
print(sort_list(a))
#5
def sumOfDigits(num):
    num=str(num)
    sum=0;
    for i in num:
        c=int(i)
        print(c)
        sum+=c
    return sum
print(sumOfDigits(23498))
#6
import random
def search(k,a):
    for i in a:
        if(i==k):
            return "Yes"
        else:
            return "No"
#7
a=[]
n=100
k=5
for i in range(0,n):
    a.append(random.randint(1,200))
print(search(k,a))
print(search(2,a))
print(a)
#8
a=[1,3,4,5,6]
b=[2,4,5,6,8,0]
c=[]
for i in a:
    for j in b:
        if(j!=0):
            c.append(i//j)
print(c)
#9
a="car"
b="CARpet"
c="abcdefghijklmnopqrstuvwxyz"
c=list(c)
for j in range(0,len(b)):
    k=ord(b[j])
    if(k<97):
        k=k-65
        b=list(b)
        b[j]=c[k]
        b="".join(b)
        #print(j)

flag=0;
for i in range(0,len(b)):
    fg=1;
    k=i
    for j in a:
        if(j!=b[k]):
            fg=0
            break
        else:
            k+=1

    if(fg==1):
        flag=1;
        print("Yes")
        break;
if(flag==0):
    print("NO")
#10
def tofloat(num):
    return float(num)
def tostring(num):
    return str(num)
a=[0,2,3,5,0,9,0]
b=map(tofloat,a)
c=map(tostring,a)
