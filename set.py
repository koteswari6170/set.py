# e={}
# print(e,type(e)) #dict
# v={1,2.6,"Hello",("hi",2)}
# print(v,type(v)) # {1, 2.6, 'Hello', ('hi', 2)} set
# n={10,20,30}
# print(n[1])#TypeError:set object is not subscriptable
# d={1,3,5}
# print(d,type(d))# {1,3,5} set
# k=frozenset(d)
# print(k[0]) #TypeError:frozenset object is not subscriptable
# a={1,2,3}
# h='hello',1,2,3
# a.add(h)
# print(a) #
# b={2,3,5}
# b.clear()
# print(b) #set()
# a={1,2,3}; b={4,3,3,6}; c={10,15,20}; d={1,4,7}
# print(a.intersection(b))#{3}
# print(a.intersection(c))#set()
# print(a.intersection(d))#{1}
# print(b.intersection(d))#{4}
# a={1,2,3}
# b={4,3,5}
# print(a.union(b))#{1,2,3,4,5}
# print(b.union(a))#{1,2,3,4,5}

# a={1,2,3}
# b={4,3,5}
# c={4,3,7}
# a.add(b)
# print(a)#TypeError:unhashable type:set
# a.update(b)
# a.update(c)
# print(a)#{1,2,3,4,5,7}

# a={5,10,20,30,34}
# b={10,20,5}
# print(a.difference(b))#{30,34}
# print(b.difference(a))#set()
# print(a-b)#{30,34}
# print(b-a)#set()

# z={55,56,57,73,45,23}
# z.discard(4)
# print(z)#{55,56,57,73,45,23}
# z.discard(56)
# print(z)#{55, 23, 73, 45, 57}

# v={26,7,11,4,23}
# v.pop()
# print(v)#{23,7,26,11}
# a={1,2,3,4}
# b={5,6,7}
# c={4,5,6}
# print(a.isdisjoint(b))#True
# print(a.isdisjoint(c))#False
# print(b.isdisjoint(c))#False
# a={1,2,3}
# b={1,2,3,4,5}
# c={1,2,4,5}
# print(a.issubset(b)) #True
# print(b.issubset(a)) #False
# print(a.issubset(c)) #False
# print(c.issubset(b)) #True
a={5,12,15,18,20}
b={15,18,21,25}
a.difference_update(b)
b.difference_update(a)
print(a)
print(b)
a.update(b)
b.update(a)
print(a)
print(b)








