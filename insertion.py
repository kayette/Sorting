# JAVIER : 54, 23, 36, 86, 19, 77, 35, 7, 48, 89
# CODE REFERENCE : https://realpython.com/sorting-algorithms-python/#the-insertion-sort-algorithm-in-python

def insertionSorting(array):

    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1

        while j >= 0 and array[j] > key_item:
          
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array

javierData = [54, 23, 36, 86, 19, 77, 35, 7, 48, 89]
size = len(javierData)
insertionSorting(javierData)
print("\nUnsorted data: [54, 23, 36, 86, 19, 77, 35, 7, 48, 89]")
print(f"The data after sorting it in ascending order by insertion algorithm is: {javierData}\n")