
# name=input("Eneter your Palindrom Name : ")
def is_palindrom(word):
     reverse = word[::-1]
 if word == reverse :
          return  True 
 else :
     return  False 

print(is_palindrom("naman"))
print(is_palindrom("horse"))
