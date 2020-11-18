
# THIS CHALLENGE 

# defined a function take any number of list containing number 
# [1,2,3] ,[4,5,6],[7,8,9]
# return average 
# (1+4+7)/3,(2,5,8)/3,(3,6,9)/3

# try to make anonymous function in one line using lambda func

# def average_finder(l1,l2):
#     average = []
#     for pair in zip(l1,l2):
#           average.append(sum(pair)/len(pair))
#     return average 

# print(average_finder([1,2,3] ,[4,5,6]))

# passing with the multiple list items 

def average_finder(*args):
    average = []
    for pair in zip(*args):
          average.append(sum(pair)/len(pair))
    return average 

print(average_finder([1,2,3] ,[4,5,6],[7,8,9]))

# using for the lambda func and comprehension 

average_finder = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder([1,2,3] ,[4,5,6],[7,8,9]))