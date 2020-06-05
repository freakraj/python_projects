
user_info = {

    'name' : 'raj gautam',
    'age' : 24,
    'fav_movie' : ['coco','kimi no na wa'],
    'fav_tunes' : ['awakening','fairy tale'],
    'mobile_no' : 9865784897
}

# # print(user_info)
# # Check if key exist in dictionary 
# # if 'fav_tunes' in user_info :   # in keyword sirf dict ki key check krega value nhi dekhega
# #      print("present")
# # else :
# #      print("not present")

# # check if value exist in dictionary  --> values method 
# if 'raj gautam' in user_info.values(): 
#      print("present")
# else :
#      print("not present")

# if 24 in user_info.values():
#     print("this age are presenting in dict ..")
# else :
#     print("not present ")

# # loop in dictionaries 
# for i in user_info :
#     print(i)   # isse kya hoga ki hmari sari key print kr dega 

# # How to print value in dictionaries using for loop 

# # for i in user_info.values() :
# #     print(i)
# # =============================================================
# # Ye the values method 
# user_values=user_info.values()
# print(user_values)
# print(type(user_values))

# # Aise hi ak keys  mehtod hai 

# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# # keys ki help se values ko print kre 
# # for i in user_info:
# #     print(user_info[i])

# # items method => return to List inside tuple 

# user_items = user_info.items()
# print(user_items)
# print(type(user_items)) #<class 'dict_items'>
# #[('name', 'raj gautam'), ('age', 24), ('fav_movie', ['coco', 'kimi no na wa']), 
# # ('fav_tunes', ['awakening', 'fairy tale']), ('mobile_no', 9865784897)])

# #--------------------------------------------------------------
# # hOW TO USE FULL ITEM METHOD 
# Very use full mehtod - items()
for key,value in user_info.items():
    print(f" key is {key} and value is {value}")

