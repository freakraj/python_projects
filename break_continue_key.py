
# break and continue key word 
# print 1 to 10

for i in range(11):
      if i == 5:
          break
      print(i)

# continue 
# print 1 to 10 ,but not 5
# ,1,2,3,4,6,7,8,9,10

for i in range(1,11):
     if i ==5:
         continue   # continue key word ne kya kiya ki print vali line execute nhi ki aur for ke pas a gya
     print(i)