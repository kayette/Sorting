# JAVIER : 54, 23, 36, 86, 19, 77, 35, 7, 48, 89
# CODE REFERENCE : https://www.freecodecamp.org/news/bubble-sort-algorithm-in-java-cpp-python-with-example-code/

def bubbleSorting(array):
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array

if __name__ == '__main__':
    javierData = [54, 23, 36, 86, 19, 77, 35, 7, 48, 89]
    print("\nUnsorted data: [54, 23, 36, 86, 19, 77, 35, 7, 48, 89]")
    print(f"The data after sorting it in ascending order by bubble algorithm is:", bubbleSorting(javierData))