def swap(a, i, j):
    a[i] = a[i] + a[j]
    a[j] = a[i] - a[j]
    a[i] = a[i] - a[j]

def quickSort(a, i, j):
    if i >= j:
        return
    first = i
    last = j
    pivot = i
    while i <= j:
        while a[j] >= a[pivot] and j != pivot:
            j-=1
        if j > pivot:
            swap(a, pivot, j)
            pivot = j
        j-=1
        while a[i] <= a[pivot] and i != pivot:
            i+=1
        if i < pivot:
            swap(a, pivot, i)
            pivot = i
        i+=1
    print(a)
    if first <= pivot-1:
        quickSort(a, first, pivot - 1)
    if pivot+1 <= last:
        quickSort(a, pivot + 1, last)

a = [1, 3, 2, 5, 4, 6, 7]
quickSort(a, 0, len(a)-1)
print(a)
