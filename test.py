list = ('test','test2', "asdasda", "dsd")

arr = {}

for word in list:
    letter = word[0]
    arr.setdefault(letter, [0]).append(word)
    
print(arr)


#array = {i+1:v for i,v in enumerate(list) if len(v) > 3}
#print (array)
#
#filter_list = [val.upper() for val in list if len(val) > 3]
#print(filter_list)
