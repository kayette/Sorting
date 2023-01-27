# JAVIER : 54, 23, 36, 86, 19, 77, 35, 7, 48, 89
# CODE REFERENCE : https://www.geeksforgeeks.org/python-program-for-quicksort/

def partition(array, low, high):
 
    pivot = array[high]
 
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
 
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1
 
def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)
 
        quickSort(array, pi + 1, high)
 
 
javierData = [54, 23, 36, 86, 19, 77, 35, 7, 48, 89]
print("\nUnsorted data: [54, 23, 36, 86, 19, 77, 35, 7, 48, 89]")
 
size = len(javierData)
 
quickSort(javierData, 0, size - 1)
print(f"The data after sorting it in ascending order by quick algorithm is: {javierData}\n")