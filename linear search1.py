def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
if __name__ =="__main__":
    arr = [5,7,8,2,6,676]
    target = int(input())
    result = linear_search(arr,target)
    if result !=-1:
        print(f"found at index {result}")
    else:
        print("not found")