
# list inside list 

matrix = [[1,2,3],[4,5,6],[7,8,9]]

# 3 item and --> 3 list 



for sublist in matrix :
    for i in sublist:
        print(i,end=" ")

# list inside list ka pertiular data pta krne ke liye  ye krte hai

print(matrix[1][1])

# Type function - Data ki type pta krne ke liye isks use krte hai

name = "raj gautam"
age =23
print(type(age))