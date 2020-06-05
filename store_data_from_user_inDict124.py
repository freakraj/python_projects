
# user_info={
#     'name':"raj gautam",
#     'age':24,
#     'address':'kanpur',
#     'fav_movie':['coco','avengers''saktiman'],
#     'fav_song':['song1','song2']
# }

user = {}

name = input('please enter your name : ')
age = input('please enter your age : ')
address = input("please enter your address :")
fav_movie = input("enter your fav movie , comma seprated :").split(",")
fav_song = input("enter your song , comma seprated :").split(",")

user['name']=name 
user['age'] = age
user['address'] = address
user['fav_movie'] = fav_movie
user['fav_song']= fav_song

# print(user)

for key,value in user.items():
    print(f"{key} : {value}")
