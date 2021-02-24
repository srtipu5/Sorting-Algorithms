def partition(l,start,end):
    pivot = l[start]
    left = start
    right = end
    while (left < right):
        while pivot >= l[left]:
           left = left + 1
        while pivot < l[right]:
            right = right - 1
        if left < right:
            l[left],l[right] =  l[right],l[left]
    l[right],l[start] = l[start],l[right]
    return right

def quick_sort(l,start,end):
    if start < end:
        p = partition(l,start,end)
        quick_sort(l,start,p-1)
        quick_sort(l,p+1,end)
    return l
l = [3,1,12,5,4,10,5,2]
n = len(l)-1
print(quick_sort(l,0,n))