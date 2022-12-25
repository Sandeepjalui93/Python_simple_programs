data1={'sandeep':22,'priyanka':26}
data2={'kremar':32}

print (data1['sandeep'])
print (data2['kremar'])

#functions

print ("length of data 1=",len(data1))
print ("length of data 2=",len(data2))

print ("string of data 1=",str(data1))
print ("string of data 2=",str(data2))

#Methods

print("Below are methods")

print("getting keys of data 1",data1.keys())
print("getting keys of data 2",data2.keys())

print("--------------")

print("getting values of data 1",data1.values())
print("getting values of data 2",data2.values())

print("--------------")

print("getting items of data 1",data1.items())
print("getting items of data 2",data2.items())

print("--------------")
data1.update(data2)
print("updating of data 1 with data 2",data1)

print("--------------")
data2.clear()
print("clearing data 2",data2)

print("--------------")

data3=data1.copy()

print("copying data 1 to data 3",data3)
print("--------------")


print("getting values",data1.get('sandeep'))
print("getting values",data1.get('priyanka'))
print("--------------")


