#1
a=5
b=6
c=a+b
print(c);

#2
a=5+5
b='5'+'5'
print(a,b)
#3
a=4
a=int(a)
def iseven(a):
    if(a%2==0):
        return True
    return False
print(iseven(a))
#4
a=4
b=5
c=4
a=int(a)
b=int(b)
c=int(c)
def isisosceles(a,b,c):
    if(a==b or b==c or a==c):
        return True
    return False
print(isisosceles(a,b,c))

#5
a=45
print(type(a))
a=int(a)
print(type(a))
def isPrime(a):
    for i in range (2,a-1):
        if(a%i==0):
            return False
    return True
print(isPrime(a))
#6
a="aba"
b=a[::-1]
print(a,b)
if(a==b):
    print(True)
else:
    print(False)
#7
a="02:40 pm"
def timeconversion(a):
    if(a[6:8]=="am"):
        if(a[0:2]=="12"):
            a=list(a)
            a[0]='0'
            a[1]='0'
            a="".join(a)
            return(a[0:6])
        else:
            return(a[0:6])
    else:
        if(a[0:2]!="12"):
            s=a[0:2]
            s=int(s)
            s=str(s)
            return(s+a[2:6])
        else:
            return(a[0:6])
print(timeconversion(a))
a="12:20 am"
print(timeconversion(a))
b="12:30 pm"
print(timeconversion(b))

#8
a=2
b=3
c=4
def rootsdecision(a,b,c):
    b=b*b
    a=a*c*4
    b=b-a
    if(b<0):
        print("Two complex roots")
    elif(b>0):
        print("Two real roots")
    else:
        print("one real root")
rootsdecision(a,b,c)
a=4
b=3
c=5
rootsdecision(a,b,c)

#9
a=100
def isleapyear(a):
    if((a%4==0 and a%100!=0) or (a%400==0)):
        print("Leap year")
    else:
        print("not leap year")

isleapyear(a)
isleapyear(2000)
isleapyear(44)

#10
a="10:40 am"
b="12:30 pm"
def timediff(a,b):
    b=timeconversion(b)
    a=timeconversion(a)
    c=a[0:2]
    c=int(c)
    c=c*60
    d=a[3:5]
    c=c+int(d)
    d=b[0:2]
    d=int(d)
    d=d*60
    e=b[3:5]
    d=d+int(e)
    c=abs(c-d)
    if(c>d):
        c=(24*60)-c;
    d=c//60
    c=c%60
    print(d,"hours",c,"minutes")
timediff(a,b)
