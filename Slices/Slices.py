#⊗pyPmSlPRS

# № 1
txt = '12345'
res = txt[1:4]
print(res)
del txt, res

# № 2
lst = [1, 2, 3, 4, 5, 6, 7]
res = lst[0:3]
print(res)
del lst, res

# № 3
lst = [1, 2, 3, 4, 5, 6, 7]
res = lst[1:5]
print(res)
del lst, res

# № 4
lst = [1, 2, 3, 4, 5, 6, 7]
res = lst[1:6]
print(res)
del lst, res


#⊗pyPmSlSP

# № 1
txt = '12345'
res = txt[1:]
print(res)
del txt, res

# № 2
lst = ['ab', 1, 'cd', 2, 'ef', 3, 4]
res = lst[3:]
print(res)
del lst, res


#⊗pyPmSlEP

# № 1
txt = '12345'
res = txt[:5]
print(res)
del txt, res

# № 2
lst = ['a', 'b', 'c', 'd', 'e']
res = lst[:2]
print(res)
del lst, res


#⊗pyPmSlNP

# № 1
txt = '123456789'
res = txt[4:-2]
print(res)
del txt, res

# № 2
lst = ['a', 'b', 'c', 'd', 'e', 'f']
res = lst[1:-2]
print(res)
del lst, res

# № 3
lst = ['a', 'b', 'c', 'd', 'e', 'f']
res = lst[-1:]
print(res)
del lst, res


#⊗pyPmSlSt

# № 1
txt = '123456789'
res = txt[0:9:2]
print(res)
del txt, res

# № 2 2,4,6,8

# № 3
lst = ['a', 'b', 'c', 'd', 'e']
res = lst[0:4:3]
print(res)
del lst, res


#⊗pyPmSlOSt

# № 1
txt = '123456789'
res = txt[1::2]
print(res)
del txt, res

# № 2
lst = [1, 2, 3, 4, 5, 6, 7]
res = lst[::2]
print(res)
del lst, res

# № 3
tpl = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
weekday = tpl[0:5]
holiday = tpl[-2:]
print(weekday)
print(holiday)
del tpl, weekday, holiday


#⊗pyPmSlWS

# № 1
lst = [1, 2, 3]
res = lst[:]
print(res)
del lst, res

# № 2
num = 4567
lst = str(num)
res = lst[:]
print(res)
del num, res, lst


#⊗pyPmSlRS

# № 1
txt = '12345'
res = txt[::-1]
print(res)
del txt, res

# № 2
lst = ['c', 'b', 'a']
res = lst[::-1]
print(res)
del lst, res

# № 3
txt = '123456789'
res = txt[-2::-2]
print(res)
del txt, res

#⊗pyPmSlER

# № 1
lst = [1, 2, 3, 4, 5, 6]
del lst[0::2]
print(lst)
del lst

# № 2
lst = [1, 2, 3, 4, 5, 6, 7, 8]
del lst[0::2]
res = lst[::-1]
print(res)
del lst, res