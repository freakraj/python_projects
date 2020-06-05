# make flexible function 

# def totale(a,b):
#   return a+b

# print(totale(5,10,10,12))

def all_totale(*args):
     totale=0

     for num in args:
        totale +=num
     return totale 

print(all_totale(1,12))