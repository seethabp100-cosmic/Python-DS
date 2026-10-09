# Insert sort with full array shifts
#
# Insertion sort works by taking one element at a time from the unsorted part
# and inserting it into the correct position in the sorted part of the array.
#
# Step-by-step algorithm:
# 1) Start from the second element (index 1) because the first element is
#    considered already sorted.
# 2) Store the current element in a variable called current_val.
# 3) Compare it with elements before it in the sorted portion.
# 4) If an earlier element is greater than current_val, shift that element one
#    position to the right to make space.
# 5) Continue moving left until you find the correct insertion spot.
# 6) Place current_val in its proper location.
# 7) Repeat this process for every remaining element.
#
# Example:
# unsortedArray = [7,12,9,11,3]
# arraySize = len(unsortedArray)
# for i in range(1, arraySize):
#     insertIndex = i
#     current_val = unsortedArray[i]
#     for j in range(insertIndex - 1, -1, -1):
#         if unsortedArray[j] > current_val:
#             unsortedArray[j + 1] = unsortedArray[j]
#             insertIndex = j
#         else:
#             break
#     unsortedArray[insertIndex] = current_val
# print("Insert Sort:: ", unsortedArray)

unsortedArray = [7,12,9,11,3]
arraySize  = len(unsortedArray)
for i in range(1,arraySize):  #  1,5
    insertIndex = i  #1
    current_val = unsortedArray[i]  #12
    for j in range(insertIndex-1,-1,-1):
        if unsortedArray[j]>current_val:
            unsortedArray[j+1] = unsortedArray[j]
            insertIndex = j
        else:
            break
    unsortedArray[insertIndex] = current_val
print("Insert Sort:: ",unsortedArray)   

