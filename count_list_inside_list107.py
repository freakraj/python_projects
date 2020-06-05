
# how to count list inside list 

# def count_list(l):
#     count = 0
#     for i in l :
#         if type(i)==list :
#             count +=1
#     return count
# mixed = [1,2,3,[1,2],[2,3,5]]

# print(count_list(mixed))


def count_inside_list(l):
    count =0

    for i in l:
        if type(i) == list:
            count +=1
    return count 
mixed = [1,2,3,4,[5,12,3],[50,30,1],[5,6]]

print(count_inside_list(mixed))