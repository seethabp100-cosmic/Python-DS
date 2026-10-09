# arr = [64, 34, 25, 5, 22, 11, 90, 12]
# n = len(arr)
# for i in range(n-1):
#     min_index = i
#     for j in range(i+1,n):
#         if arr[j] < arr[min_index]:
#              min_index = j 
#     minVal = arr.pop(min_index)
#     arr.insert(i, minVal)
    
# print("Sorted: ",arr)


unsortedArray = [7,12,9,11,3]
arraySize = len(unsortedArray)

for i in range(arraySize-1):
    minIndex = i
    for j in range(i+1,arraySize):
        if unsortedArray[j]<unsortedArray[minIndex]:
            minIndex = j
    # minimumVal = unsortedArray.pop(minIndex)
    # unsortedArray.insert(i,minimumVal)
    unsortedArray[i], unsortedArray[minIndex] = unsortedArray[minIndex], unsortedArray[i]
print("Selection Sorted:: ",unsortedArray)