'''
CountSorting: Algorithm
1) Get a array with unsorted Elements
2) Extract max element from the current array and create count array with index of max+1
3) Iterate the current array and increment the elements in count array with respect to the element from current array as index or count array.
4) Clear the elements in current array, and add sorted elements according to the count data in count array
'''

def countSort(array):
    if not array:
        return array

    maxNum = max(array)
    count = [0]*(maxNum+1)
    for num in array:
        count[num]+=1
        print("count array: ",count)

    array[:] = []
    for num, freq in enumerate(count):
        array.extend([num]*freq)

    return array


array = [3,9,1,7,1,3,3,4,7,7,0,6,2,6]
sortedArray = countSort(array);
print("Sorted:: ",sortedArray)