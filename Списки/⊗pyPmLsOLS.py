# № 1
lst = [4, 2, 5, 1, 3]
lst.sort()
print(lst)
del lst

# № 2
lst = [4, 2, 5, 1, 3]
lst.sort(reverse=True)
print(lst)
del lst

# № 3
lst = [1, 2, 3, 4, 5]
lst.sort(reverse=True)
print(lst)
del lst

# № 4
lst1 = ['a', 'b', 'c']
lst2 = [3, 2, 1]
lst1.sort(reverse=True)
lst2.sort()
lst2 += lst1
print(lst2)