a=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
b=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for i in a:
    print(i)
for i in range(0,3):
    for j in range(0,4):
        b[j][i]=a[i][j]
print(b)
