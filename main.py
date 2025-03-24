def equilibriumpoint(arr):
    leftsidesum=0
    rightsidesum=0
    n=len(arr)
    for i in range(0,n):
        leftsidesum=0
        rightsidesum=0
        for j in range(i):
            leftsidesum+=arr[j]
        for j in range(i+1,n):
            rightsidesum+=arr[j]
        if leftsidesum==rightsidesum:
            return i
    return -1
arr=[4,6,0,5,4,1]
print(equilibriumpoint(arr))
#tells the answer according to the index or position of the equilibrium point in the array