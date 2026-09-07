#⊗pyPmDcInr

# № 1
dct = {}
dct[1] = 'a'
dct[2] = 'b'
dct[3] = 'c'
print(dct)
del dct

# № 2
dct = {}
dct[2] = 'ab'
dct[4] = 'cd'
dct[6] = 'ef'
print(dct)
del dct

# № 3
dct = {}
dct['surname'] = 'Be'
dct['name'] = 'Eve'
dct['age'] = 'Val'
print(dct)
del dct

# № 4
dct = {}
dct.update({1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'})
print(dct)
del dct


#⊗pyPmDcACr

# № 1 - {'a': 1, 'b': 2, 'c': 3}
# № 2 - {'1': 'a', '2': 'b', '3': 'c'}
# № 3 - {'a': '12', 'b': '34', 'c': '56'}
# № 4 - error


#⊗pyPmDcEV

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(dct['x'])
print(dct['y'])
print(dct['z'])
del dct

# № 2
dct = {
	'a': 1,
	'b': 2,
	'c': 3
}
print(dct['b'])
del dct

# № 3
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
key = 'x'
print(dct[key])
del dct

# № 4
dct = {
	'a': 5,
	'b': 10,
	'c': 15
}
i = dct['a']
k = dct['b']
j = dct['c']
res = i + k + j
print(res)
del dct, i, k, j, res

# № 5
dct = {
	1: 'a',
	2: 'b',
	3: 'c'
}
i = dct[1]
k = dct[2]
j = dct[3]
res = i + k + j
print(res)
del dct, i, k, j, res


#⊗pyPmDcEVCh

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
dct['x'] += 1
print(dct)
del dct

# № 2
dct = {
	'surn': 'smit',
	'name': 'john'
}
dct['surn'] = 'Be'
dct['name'] = 'Eve'
print(dct)
del dct


#⊗pyPmDcEA

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
dct[1] = 'a'
dct[2] = 'b'
dct[3] = 'c'
print(dct)
del dct


#⊗pyPmDcLn

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(len(dct))
del dct

# № 2
dct1 = {
	'a': 12,
	'b': 34,
	'c': 56,
	'd': 78,
	'e': 90
}
dct2 = {}
dct2['dct1'] = len(dct1)
print(dct2)
del dct1, dct2


#⊗pyPmDcLn

# № 1
dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}
dct2 = {
	'x': 4,
	'y': 5,
	'z': 6
}
dct1.update(dct2)
print(dct1)
del dct1, dct2

# № 2
dct1 = {
	'3': 'c',
	'4': 'd',
	'5': 'e'
}
dct2 = {
	'1': 'a',
	'2': 'b'
}
dct2.update(dct1)
print(dct2)
del dct1, dct2

# № 3
dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}
dct2 = {
	'x': 4,
	'y': 5,
	'z': 6
}
dct3 = {}
dct1.update(dct2)
dct3.update(dct1)
print(dct3)
del dct1, dct2, dct3

# № 4
dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}
dct2 = {
	'd': 4,
	'e': 5,
	'f': 6
}
dct3 = {
	'j': 7,
	'h': 8,
	'i': 9
}
dct1.update(dct2)
dct1.update(dct3)
print(dct1)
del dct1, dct2, dct3


#⊗pyPmDcSEC

# № 1 - {'z': 6, 'w': 8, 'f': 10, 'x': 4, 'y': 5}
# № 2 - {1: 'd', 3: 'e', 4: 'f', 7: 'j', 2: 'a', 4: 'b', 6: 'c'}


#⊗pyPmDcRBK

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
del dct['x']
print(dct)
del dct

# № 2
dct = {
	1: 'a',
	2: 'b',
	3: 'c',
	4: 'd',
	5: 'e'
}
del dct[2]
del dct[4]
print(dct)
del dct


#⊗pyPmDcEBK

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(dct.pop('x'))
del dct

# № 2 - error
# № 3 - {'name': 'john','age': 30}


#⊗pyPmDcLEE

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(dct.popitem())
del dct

# № 2
dct = {
	1: 'a',
	2: 'b',
	3: 'c',
	4: 'd',
	5: 'e'
}
lst = list(dct.popitem())
lst += list(dct.popitem())
lst += list(dct.popitem())
lst += list(dct.popitem())
lst += list(dct.popitem())
del lst[1], lst[2], lst[3], lst[4], lst[5]
print(lst)
del dct, lst


#⊗pyPmDcAER

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
dct.clear()
print(dct)
del dct

# № 2 - dct = {4: 'text4'}


#⊗pyPmDcEP

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print('x' in dct)
del dct

# № 2 - False
# № 3 - True
# № 4 - True


#⊗pyPmDcOEG

# № 1 - 'w'
# № 2 - None
# № 3
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
print(dct.get('w', '!'))
del dct


#⊗pyPmDcCTL

# № 1
dct = {
	1: 'ab',
	2: 'cd',
	3: 'ef'
}
res = list(dct)
print(res)
del dct, res

# № 2
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = list(dct)
res.reverse()
print(res)
del dct, res


#⊗pyPmDcKG

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = dct.keys()
print(res)
del dct, res

# № 2
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
res = dct.keys()
print(res)
del dct, res

# № 3
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = list(dct.keys())
print(res)
del dct, res

# № 4
dct = {
	2: 'ab',
	4: 'cd',
	6: 'ef'
}
lst = list(dct.keys())
res = lst[0] * lst[1] * lst[2]
print(res)
del dct, res, lst

# № 5
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
lst = list(dct.keys())
lst.reverse()
print(lst)
del dct, lst


#⊗pyPmDcAVG

# № 1
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = dct.values()
print(res)
del dct, res

# № 2
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
res = dct.values()
print(res)
del dct, res

# № 3
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = list(dct.values())
print(res)
del dct, res

# № 4
dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}

dct2 = {
	1: 'a',
	2: 'b',
	3: 'c'
}
lst1 = list(dct1.values())
lst2 = list(dct2.values())
res = lst1 + lst2
print(res)
del dct1, dct2, res, lst1, lst2


#⊗pyPmDcKVG

# № 1
dct = {
	'x': 3,
	'y': 2,
	'z': 1
}
res = dct.items()
print(res)
del dct, res

# № 2
dct = {
	'a': [2, 4],
	'b': [3, 5]
}
res = dct.items()
print(res)
del dct, res

# № 3
dct = {
	1: 'x',
	2: 'y',
	3: 'z',
	4: 'w'
}
res = list(dct.items())
print(res)
del dct, res

# № 4
dct = {
	'a': 12,
	'b': 34,
	'c': 56
}
lst = list(dct.items())
res = lst[0] + lst[1] + lst[2]
print(list(res))
del dct, res, lst


#⊗pyPmDcCTD

# № 1 - {1: 'ab', 2: 'cd', 3: 'ef'}
# № 2 - {'x': 2, 'y': 4, 'z': 6}
# № 3 - error
# № 4 - {'a': 1, 'b': 2, 'c': 3}


#⊗pyPmDcPrm

# № 1
dct = {
	'x': '1',
	'y': '2',
	'z': '3'
}
lst = list(dct.values())
res = (int(lst[0]) ** 2) + (int(lst[1]) ** 2) + (int(lst[2]) ** 2)
print(res)
del dct, res, lst

# № 2
dct1 = {
	'1': 12,
	'2': 24,
	'3': 36
}

dct2 = {
	'a': '3',
	'b': '6',
	'c': '9'
}
lst1 = list(dct1.values())
lst2 = list(dct2.values())
sum1 = lst1[0] + lst1[1] + lst1[2]
sum2 = int(lst2[0]) + int(lst2[1]) + int(lst2[2])
res = sum1 - sum2
print(res)
del dct1, dct2, res, lst1, lst2, sum1, sum2

# № 3
dct = {
	1: '4',
	2: '5',
	3: '6'
}
dct[str(1)] = dct[1]
dct[str(2)] = dct[2]
dct[str(3)] = dct[3]
del dct[1], dct[2], dct[3]
print(dct)
del dct

# № 4
dct = {
	'x': 1,
	'y': 2,
	'z': 3
}
res = str(dct['x']) + str(dct['y']) + str(dct['z'])
print(res)
del dct, res

# № 5
dct = {
	'a': 7,
	'b': 6,
	'c': 5
}
lst = list(dct.values())
lst.reverse()
lst[0] = str(lst[0])
lst[1] = str(lst[1])
lst[2] = str(lst[2])
res = '/'.join(lst)
print(res)
del dct, lst

# № 6
dct = {
	'y': 2025,
	'm': 12,
	'd': 31
}
lst = list(dct.values())
lst[0] = str(lst[0])
lst[1] = str(lst[1])
lst[2] = str(lst[2])
res = '-'.join(lst)
print(res)
del dct, lst