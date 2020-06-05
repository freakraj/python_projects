
# def word_counter(s):

#     count = {}
#     for char in s:
#         count[char]=s.count(char)
#     return count
# print(word_counter("harshit"))

# word count 

# def word_counter(s):
#     count= {}
#     for char in s:
#         count[char]=s.count(char)
#     return count
# print(word_counter("harshit"))

def cube(n):
    number={}
    for i in range(1,n+1):
        number[i]=i**3
    return number
print(cube(10))