arr=[0,1,0,1,0,1,0,0,0,1,1]
zeroflips=0
oneflips=0
n=len(arr)
for i in range(n):
    if arr[i]==0:
        zeroflips+=1
    if arr[i]==1:
        oneflips+=1
print("The number of flips required to change zeros:",zeroflips,"and the number of flips required to change the ones:",oneflips)