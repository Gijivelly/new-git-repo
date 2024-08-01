lst = [1,2,3,4,3,4,5]
count_num = {}
for i in lst:
    if i in count_num:
        count_num[i]+=1
print(count_num)