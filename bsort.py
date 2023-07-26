def bosrt(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
arr = [67,90,68,68,89]
bosrt(arr)
print(arr)
#second method

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


try:
    arr = list(map(int, input("Enter space-separated numbers for the array: ").split()))
except ValueError:
    print("Invalid input. Please enter space-separated numbers only.")
    exit(1)

bubble_sort(arr)
print("Sorted array:", arr)