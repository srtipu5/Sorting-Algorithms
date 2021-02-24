def Insertion_Sort(list):
    for i in range(1,len(list)):
        min_value = list[i]
        j = i-1
        while j >= 0 and min_value < list[j]:
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = min_value
    return list
list = [5,2,1,6,9,8]
print(Insertion_Sort(list))