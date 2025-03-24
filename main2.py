def subarraysum(arr,n,sum_):
    for i in range(n):
        currsum=arr[i]
        j=i+1
        while j<=n:
            if currsum==sum_:
                print("sum found between")
                print("the indexes %d and %d"%(i,j-1))
                return 1
            if currsum>sum_ or j==n:
                break
            currsum+=arr[j]
            j+=1
    print("no subarray found")
    return 0
arr=[3,6,5,4,7,6,0,1,2,5]
sum_=15
n=len(arr)
subarraysum(arr,n,sum_)


