def merge_sorted_arrays(array1, array2):
    new_array = []
    first_array_index = 0
    second_array_index = 0
    flag = 0

    while first_array_index < len(array1) and second_array_index < len(array2):
        if array1[first_array_index] <= array2[second_array_index]:
            new_array.append(array1[first_array_index])
            first_array_index += 1
        else:
            new_array.append(array2[second_array_index])
            second_array_index += 1

    if first_array_index == len(array1) - 1:
        flag = 1

    if flag == 0:
        for i in range(second_array_index, len(array2)):
            new_array.append(array2[i])
    else:
        for i in range(first_array_index, len(array1)):
            new_array.append(array1[i])

    return new_array
    

array1 = [1,3,5,7, 13]
array2 = [1,2,4,6,8,10,12]
print(merge_sorted_arrays(array1,array2))
# [1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13]