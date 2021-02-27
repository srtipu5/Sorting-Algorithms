def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        min_value = a[i]
        j = i -1
        while j >=0 and min_value < a[j]:
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = min_value
    return a
a = [5,6,7,1,10,22,3]
print(insertion_sort(a))