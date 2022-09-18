# list-> ordered collection of datatypes,[],mutable(changeable)

list1=["america","japan","india",573,456.324,True] 
print(list1)

#slicing
print(list1[1:3])
print(list1[-4:-1])

#step index
print(list1[1:4:2])
print(list1[-5:-2:2])

# Update
list1[3]=False
print(list1)

# Append 
list1.append("cake")
print(list1)

#Insert
list1.insert(3,"france")
print(list1)

# delete
del list1[0]
print(list1)

#remove
list1.remove("japan")
print(list1)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////



#Tuple ->ordered collection of datatypes ,(), immutable

tuple1=("ironman","hawkeye","balckwidow","spiderman",201,90.345,True)
print(tuple1)
print(len(tuple1))


#slicing
print(tuple1[1:3])
print(tuple1[-4:-1])

#step index
print(tuple1[1:4:2])
print(tuple1[-5:-2:2])
#update 
# tuple1[4]=True //does not support update statement
tuple2=list(tuple1)
tuple2[4]=True
print(tuple2)

#append
# tuple1.append("thor") //does not support append statement
tuple2.append("thor")
print(tuple2)
#insert
# tuple1.insert(4,"thor") //does not support insert statement
tuple2.insert(5,"rocket")
print(tuple2)
#delete
del tuple1
#print(tuple1)

#remove
#tuple1.remove("hawkeye")// does not support remove statement
#print(tuple1)

#///////////////////////////////////////////////////////////////////////////////////////////

#Dictionary : it consists of key and the values
#it cannot perform slicing operation

Dict={
    "name":"tony",
      "company":"stark industries",
      "other name":"ironman",
      "current armour":"mark 85",
      "software":"friday",
      "year":2008,
      "automatic":True
    
}
print(len(Dict))
print(Dict["name"])

#add
Dict["previous software"]="abd" #duplicates are not allowed
Dict["previous software"]="jarvis"
print(Dict)

del Dict["previous software"]
print(Dict)

#update
Dict.update({"year":2019})
print(Dict)

#pop
Dict.pop("year")
print(Dict)

#///////////////////////////////////////////////////////////////////////////////////////////////

#set->unordered collection of data types,{}
set1={"x","y","z",23456,456.21,True}
print(set1)
print(len(set1))

#update
# set1.add(True) //does not allow duplicates
set1.add(False)
print(set1)

#/////////////////////////////////////////////////////////////////////////////////////////////////

# Frozensets
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copy
C = A.copy()
print(C)

# union
print(A.union(B))

# intersection
print(A.intersection(B))

# difference
print(A.difference(B))  

# symmetric_difference
print(A.symmetric_difference(B))

#///////////////////////////////////////////////////////////////////////////////////////////////////
