def sel(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
            
input=input("nu")
arr=list(map(int,input.split()))
print("or: ",arr)
sel(arr)
print("so ",arr)