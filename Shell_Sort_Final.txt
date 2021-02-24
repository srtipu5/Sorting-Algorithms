def Shell_Sort(list):
    gap = len(list)//2
    while gap > 0:
        for i in range(gap,len(list),gap):
            min_value = list[i]
            j = i - gap
            while j >= 0 and min_value < list[j]:
                list[j+gap] = list[j]
                j = j - gap
            list[j+gap] = min_value
        gap = gap//2
    return list
list = [5,2,1,6,9,8]
print(Shell_Sort(list))