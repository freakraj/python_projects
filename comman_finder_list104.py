
def comman_finder_list(l1,l2):
    output =[]
    for i in l1:
        if i in l2 :
            output.append(i)
    return output 

num1_list =[1,2,3,5,8]
num2_lsit = [1,2,5,8,9,2]

print(comman_finder_list(num1_list,num2_lsit))