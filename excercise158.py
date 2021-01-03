# this is challenge 
#--------------------
# defined a function take any number of lists containing number 
# [1,2,3],[4,5,6],[7,8,9]
# return average 
# (1,4,7)/3 ,(2,5,8)/3 , (3,6,9)/3

# try to make  this anonymous function in one line using lambda 

# this function average for the two list 
#========================================
def average_finder(l1,l2):
    average = []
    for pair in zip(l1,l2):
        average.append(sum(pair)/len(pair))
    return average
print(average_finder([1,2,3],[4,5,6]))

multiple list to find average 
#===================================
def average_multiList(*args):
    averageEmp = []

    for pair in zip(*args):
        averageEmp.append(sum(pair)/len(pair))
    return averageEmp
print(average_multiList([2,3,5],[3,2,5],[5,1,6]))

# solve this problem to single line 
#========================================
average_finder = lambda *args :[sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder([1,2,3],[4,5,6],[7,8,9]))

# practice for the repeted solution 
list1 = [1,2,3,4]
list2 = [4,5,6,8]
def average_finder(*args):
    averge = []
    for pair in zip(*args):
        averge.append(sum(pair)/len(pair))
    return averge
print(average_finder(list1,list2,[7,8,9,5],[12,21,12,10]))


average_finder = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder([2,4,4,5],[4,56,33],[4,56,6]))


