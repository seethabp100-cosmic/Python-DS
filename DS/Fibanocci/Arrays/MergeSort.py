def mergeSort(arr):
    if len(arr)<=1:
        print("array with length 1: ",arr)
        return arr

    mid = len(arr)//2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    print("left half: ", leftHalf)
    print("right half: ", rightHalf)
    sortleft = mergeSort(leftHalf)
    sortright = mergeSort(rightHalf)

    return merge(sortleft, sortright)

def merge(sortleft, sortright):
    result = []
    i = j = 0
    while i<len(sortleft) and j<len(sortright):
        if sortleft[i] < sortright[j]:
            result.append(sortleft[i])
            i+=1
        else:
            result.append(sortright[j])
            j+=1
    result.extend(sortleft[i:])
    result.extend(sortright[j:])

    return result

array = [3, 7, 6, -10, 15, 23.5, 55, -13]
result = mergeSort(array)
print("Sorted array: ",result)