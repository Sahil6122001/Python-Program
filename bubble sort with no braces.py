def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j +1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
arr = [45,67,89,88]
bubble(arr)
output = ' '.join(map(str, arr))
print(output)
print(arr)
print(type(output))