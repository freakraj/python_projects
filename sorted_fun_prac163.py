# sorted function Practice 
fruits = ['mango','grapes','apple']
fruits.sort()
print(fruits)

# this is a tuple 
fruits2 = ('mango','grapes','apple')
print(sorted(fruits2))

# this is set 
fruits3 = {'mango','apple','banana'}
print(sorted(fruits3))

guitar = [
    {'model':'yamaha f31','price':8400},
    {'model':'faith naptune','price':50000},
    {'model':'faith apolo venus','price':35000},
    {'model':'taylore','price':4500000}
]    

sorted_guitar = sorted(guitar , key=lambda item:item["price"],reverse=True)
print(sorted_guitar)



