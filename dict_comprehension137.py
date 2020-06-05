# list comprehension 
# squre = {1:1, 2:4, 3:9 }

# print the number in 1 to 10 key number value suqre 

squre = {f"Suare of {num}":f"this is square no {num**2 }"for num  in range(1,11)}
# print(squre)

for j,k in squre.items() :
    print(f"{j}:{k}")


# for k,j in suqre :
#     print(f"k")