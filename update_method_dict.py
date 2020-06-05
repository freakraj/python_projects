# Upadte mehtod in dictionary 

user_info = {
    'name' : 'raj gautam',
    'age' : 24,
    'fav_movie' : ['coco','3 idiot','avenger'],
    'fav_tune': ['sun sine','awaking','rimghim'],
}

more_info = {
    'name' : 'Harshit Vasistha',
    'hobbie' : ['coding','Dancing','Singing']
}

user_info.update(more_info)
print(user_info)