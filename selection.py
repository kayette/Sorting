# JAVIER : 54, 23, 36, 86, 19, 77, 35, 7, 48, 89
# CODE REFERENCE : https://www.geeksforgeeks.org/python-program-for-selection-sort/

def selectionSorting(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):

            if array[j] < array[min_index]:
                min_index = j
         
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
javierData = [54, 23, 36, 86, 19, 77, 35, 7, 48, 89]
size = len(javierData)
selectionSorting(javierData, size)
print("\nUnsorted data: [54, 23, 36, 86, 19, 77, 35, 7, 48, 89]")
print(f"The data after sorting it in ascending order by selection algorithm is: {javierData}\n")