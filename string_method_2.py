
# replace() Method 
# find()    Method 

string="She is beautifull and She is good dancer is"

print(string.replace(" ","_"))
print(string.replace("She","raj",1))
print(string.replace(" ",""))

print(string.find("is"))

is_pos1=string.find("is")
print(string.find("is",is_pos1+1))

is_post2=string.find("is",is_pos1+1)

print(string.find("is",is_post2+1)) # third (is) postion find 

print(string.replace("beautifull","raj"))