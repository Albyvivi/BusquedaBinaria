def binary_search(arr, low, high, x):
    if high>= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid -1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else: 
        return -1

arr = [11, 17, 19, 98, 200]
x = 17

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Elemento se encuentra en la posición", str(result), "dentro del arreglo")
else: 
    print("Elemento no consta dentro del arreglo")