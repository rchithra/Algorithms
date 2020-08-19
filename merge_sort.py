def merge(arr):
    print(arr)
    if (len(arr) < 2):
        return arr
    m = int(len(arr)/2)
    result = []
    left = merge(arr[:m])
    right = merge(arr[m:])
    print (left)
    print (right)
    while (len(left) > 0 and len(right) > 0):
        if ( left[0] < right[0]):
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    result += left
    print(result)
    result += right
    print (result)
    return result

for i in merge([3,2,5,7,9,10,3,1,7,6,4,3]):
    print(i)