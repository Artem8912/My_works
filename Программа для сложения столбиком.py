def List(length):
    list1=[]
    i = 0
    while i < length:
        list1.append(int(input(f"Введите элемент № {i+1}: ")))
        i+=1
    print (list1)
    return list1
def SumList(length1,length2):
    sum_list = []
    i = 0
    lengthm = max(length1,length2)
    length = min(length1,length2)
    while i <length:
        sum_list.append(int(b1[len(b1)-i-1]) + int(b2[len(b2)-i-1]))
        i+=1
    for i in range(length,lengthm,1):
        if len(b1)>len(b2):
            sum_list.append(b1[len(b1)-i-1])
        elif len(b2)>len(b1):
            sum_list.append(b2[len(b2)-i-1])  
    for i in range(0,lengthm,1):    
        if sum_list[i] >9 and i < lengthm-1:
            sum_list[i] = sum_list[i]%10
            sum_list[i+1]+=1
        elif sum_list[lengthm-1] >9:
            sum_list[lengthm-1] = sum_list[lengthm-1]%10
            sum_list.append(1)
    sum_list.reverse()  
    return sum_list 
length_list1 = int(input("Введите длину первого списка "))
b1 = List(length_list1)
length_list2 = int(input("Введите длину второго списка "))    
b2 =List(length_list2)

print("Сумма равна:")
print(SumList(length_list1,length_list2))