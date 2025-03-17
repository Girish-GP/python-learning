marks = {
    'harry':100,
    'ron':120,
    'hermione':110,
    0:'test'
}

#items() --> gives list of tuples of key value pairs
print(marks.items()) #dict_items([('harry', 100), ('ron', 120), ('hermione', 110), (0, 'test')])
for key,value in marks.items():
    print(f"Key:{key} & Value:{value}")

#keys() ---> gives list of keys
print(marks.keys()) #dict_keys(['harry', 'ron', 'hermione',

#values() ---> gives list of values
print(marks.values()) #dict_values([100,200,110,'test'])

#update() ---> updates the existing keys and adds new key
marks.update({'ron':"updated",'ggp':'newValueKey'})
print(marks) #{'harry': 100, 'ron': 'updated', 'hermione': 110, 0: 'test', 'ggp': 'newValueKey'}


#get() --> returns the value of the key specified
print(marks.get('harry')) #100

#Difference between marks.get('harry2') vs marks['harry2']
#marks.get('harry2') returns None if key is not present
#marks['harry2'] throws KeyError if key is not present

#pop()
print(f"Pop method : {marks.pop('harry')}")
print(marks)

#popitem()
print(f"popitem method last item: {marks.popitem()}")
print(f"popitem method specified item: {marks.popitem('ron')}")