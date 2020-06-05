
# add and delete data from dictionaries 

user_info = {
    'name' : 'raj gautam',
    'age' : 24,
    'fav_movie' : ['coco','kimi no na wa'],
    'fav_tune' : ['awakening','fairy tale']

}

# how to add data 

user_info['fav_song']=['song1','song2']
print(user_info) 

# Using for pop method 

poped_item =user_info.pop('fav_tune')
print(f"Pop item is {poped_item}")
print(user_info)

# how to use  popitem 
# pop item key value pair ko delete krne ke liye use krte hai 

popped_item = user_info.popitem()
print(user_info)
print(type(popped_item)) # return for tuple 