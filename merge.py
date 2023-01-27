# JAVIER : 54, 23, 36, 86, 19, 77, 35, 7, 48, 89
# CODE REFERENCE : https://www.programiz.com/dsa/mergeSorting-sort

def mergeSorting(array):
    if len(array) > 1 :
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSorting(L)
        mergeSorting(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def print_list(array):
    for i in range(len(array)):
        print(array[i], end="")

    print()

if __name__ == '__main__':
    javierData = [54, 23, 36, 86, 19, 77, 35, 7, 48, 89]

    mergeSorting(javierData)

    print("\nUnsorted data: [54, 23, 36, 86, 19, 77, 35, 7, 48, 89]")
    print(f"The data after sorting it in ascending order by merge algorithm is: {javierData}\n")