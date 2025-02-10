def mergeSort(array):
    if len(array) <= 1:
        return array
    
    #split the array into two, just the indecies
    mid = len(array) // 2 #divide it completely ignore one half keep breaking the other half
    left_half = array[:mid] #without mid
    right_half = array[mid:] #with mid
    
    print("left half is "+left_half+"right half is"+right_half )
    return left_half, right_half


def merge(left, right):
    sorted_array=[]
    i=j=0
    
    #merge elemenets from left and right

    # Merge elements from left and right in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add any remaining elements from the left half
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # Add any remaining elements from the right half
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

# Example usage:
array = [2,3,1,3,4,50,0]
sorted_array = mergeSort(array)
print("Sorted Array:", sorted_array)
    