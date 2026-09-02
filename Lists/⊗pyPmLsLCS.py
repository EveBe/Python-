# № 1
lst = ['a', 'b', 'c', 'd', 'e']
res = '-'.join(lst)
print(res)
del lst, res

# № 2 - 'a 1 b 2'
# № 3 - error

# № 4
lst = ['4', '3', '2', '1']
lst.reverse()
res = ''.join(lst)
print(res)
del lst, res