def main():
    arr = [18, 30, 15, 70, 12]
    k = 2  # Index of the element to delete (30 in this case)
    n = 5

    print("Given array elements are:")
    for i in range(n):
        print(f"arr[{i}] = {arr[i]}, ", end="")

    j = k

    while j < n:
        arr[j - 1] = arr[j]
        j = j + 1

    n = n - 1

    print("\nElements of the array after deletion:")
    for i in range(n):
        print(f"arr[{i}] = {arr[i]}, ", end="")


if __name__ == "__main__":
    main()
#second method

arr = [1,3,4]
arr.pop(int(input("enter the index ")))
print(arr)