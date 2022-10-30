def linear_search(arr, item):
    for i in range(0, len(arr)):
        if arr[i] == item:
            return i

    return -1


arr = [33, 44, 55, 66, 77, 88, 102, 301]
item = int(input("Enter you requirement item ! \n"))
result = linear_search(arr, item)

if result == -1:
    print("item not found")
else:
    print(f"Item found at index => {result}")