define a function that take of list of string 
list containing revers of every string 

Note - use list comprehension because 
Using normal method 

exp -

l=['abc','tuv','xyz']
reverse_string() ---> ['cba','vut','zyx']

def reverse_string(l):
     empty_list = []
     for i in l:
      empty_list.append(i[::-1])
     return empty_list
word = ['this','raj','disha']
print(reverse_string(word))

list comprehension 

def reverse_string1(l):
        
      reverse_string =[i[::-1]  for i in l ]
      return reverse_string
word = ['raj gautam','disha gautam','april']
print(reverse_string1(word))
    

list comprihension for reverse string element

def reverse_string(l):
       element = []
       for i in l :
           element.append(i[::-1])
       return element
word = ['raj','disha','ekta']
print(reverse_string(word)

std_name = ["rohit" , "mohit" ,"herra"]

name = []
for i in std_name:
    name.append(i[0])
print(name)

name = [i[0] for i in std_name]
print(name)

def reverse_string(l):
    return [name[::-1] for name in l]
print(reverse_string(std_name))

std_name= input("PLEASE eNTER YOUR NAME COMMA SAPRATE : ").split(",")
reversed1 = list(std_name)
def reverse_string(l):

    empty1 = []
    for i in l:    
         empty1.append(i[::-1])
    return empty1 
print(reverse_string(reversed1))




