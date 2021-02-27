def Selection_Sort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i],list[min_index]=list[min_index],list[i]
    return list
list = [5,2,1,6,9,8]
print(Selection_Sort(list))