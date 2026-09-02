# № 1
lst = ['a', 'b', 'c', 'd', 'e']
lst.remove('c')
print(lst)
del lst

# № 2
lst = ['a', 'b', 'c', 'd', 'e']
lst.remove('b')
print(lst)
del lst

# № 3
lst = ['b', 1, 2, 'b', 'c', 2]
lst.remove('b')
lst.remove('b')
lst.remove(2)
lst.remove(2)
print(lst)
del lst