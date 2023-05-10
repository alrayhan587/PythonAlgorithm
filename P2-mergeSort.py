def mergeSort(arr):
    if len(arr) > 1:

        # This part for dividing the value
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        # This part shows conquer part
        i = j = k = 0

        # At the conquer section sorting happening here
        while i < len(L) and j < len(R):

            # To create ascending or descending order
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1

            #
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len[L]:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len[R]:
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# this __name__='__main__' written for reason. If we import this file somewhere else. this code won't run (automitacally)
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]

    print("Given array is", end="")
    printList(arr)
    mergeSort(arr)

    print("Sorted Array is:", end="")
    printList(arr)
