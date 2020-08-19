def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(len(arr)-1, i, -1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
arr = [2,1,5,4,6,8,6,2,5,9,7,9,8,3]
new_arr = bubble_sort(arr)
print(new_arr)