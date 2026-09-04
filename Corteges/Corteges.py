#⊗pyPmTpCr

# № 1 - Corteges
# № 2 - Lists
# № 3 - Corteges


#⊗pyPmTpACr

# № 1
tst = '12345'
tpl = tuple(tst)
print(tpl)
del tst, tpl

# № 2
txt = '12345'
tpl = tuple(txt)
print(tpl)
del txt, tpl

# № 3
tst = 98765
tpl = tuple(str(tst))
print(tpl)
del tst, tpl


#⊗pyPmTpOET

# № 1 - string
# № 2 - Corteges
# № 3 - Boolean


#⊗pyPmTpAS

# № 1 - Corteges
# № 2 - Lists
# № 3 - string


#⊗pyPmTpEl

# № 1
tpl = (1, 2, 3, 4)
print(tpl[0])
del tpl

# № 2
tpl = ('a', 'b', 3, 4, 'c')
print(tpl[2])
del tpl

# № 3
tpl = (10, 9, 8, 7, 6)
print(tpl[-1])
del tpl

# № 4
tpl = (10, 9, 8, 7, 6)
print(tpl[-2])
del tpl

# № 5
tpl = (1, 2, 3)
print(tpl[0] + tpl[1] + tpl[2])
del tpl


#⊗pyPmTpECh

# № 1 - 'cd'
# № 2 - error and 14


#⊗pyPmTpLn

# № 1
tpl = ('1', 'b', '3', 'd', '5')
print(len(tpl))
del tpl

# № 2
tpl = (1, 2, 3)
print(len(tpl))
del tpl


#⊗pyPmTpTC

# № 1
tpl1 = ('1', '2', '3')
tpl2 = ('4', '5', '6')
tpl3 = ('7', '8', '9')
tpl = tpl1 + tpl2 + tpl3
print(tpl)
del tpl, tpl1, tpl2, tpl3

# № 2
tpl1 = (3, 4)
tpl2 = (1, 2)
tpl3 = tpl2 + tpl1
print(tpl3)
del tpl1, tpl2, tpl3


#⊗pyPmTpMl

# № 1
tpl1 = ('1', '2', '3')
tpl = tpl1 * 3
print(tpl)
del tpl, tpl1

# № 2
tpl1 = ('a', 'b')
tpl2 = (1, 2)
tpl3 = (tpl1 * 2) + tpl2
print(tpl3)
del tpl1, tpl2, tpl3


#⊗pyPmTpEP

# № 1
tpl = (2, 4, 6, 10)
res = 8 in tpl
print(res)
del tpl, res

# № 2
tpl = ('abc', 'def')
res = 'd' in tpl
print(res)
del tpl, res

# № 3 - False
# № 4 - True, False


#⊗pyPmTpUP

# № 1
tpl = ('john', 'smit')
Name, Surname  = tpl
print(Name, Surname)
del tpl, Name, Surname

# № 2
tpl = (2, 6, 14)
txt1, txt2, txt3 = tpl
res = txt1 + txt2 + txt3
print(res)
del tpl, txt1, txt2, txt3, res


#⊗pyPmTpCT

# № 1
tst = ['a', 'b', 'c', 'd']
tpl = tuple(tst)
print(tpl)
del tpl, tst

# № 2
tst = 'abcde'
tpl = tuple(tst)
print(tpl)
del tpl, tst

# № 3
tst = 12345
tpl = tuple(str(tst))
print(tpl)
del tpl, tst


#⊗pyPmTpTCL

# № 1
tpl = ('2', '6', '12')
res = list(tpl)
print(res)
del tpl, res

# № 2
tpl1 = ('1', '2', '3')
tpl2 = ('4', '5')
res = list(tpl1) + list(tpl2)
print(res)
del tpl1, res, tpl2

# № 3
tpl = (1, 2, 3, 4, 5)
res = list(tpl)
res.reverse()
tpl = tuple(res)
print(tpl)
del tpl, res


#⊗pyPmTpTCS

# № 1
tpl = ('1', '2', '3', '4', '5')
txt = '-'.join(tpl)
print(txt)
del tpl, txt

# № 2
tpl = ('1', '2', '3', '4', '5')
txt = ''.join(tpl)
print(txt)
del tpl, txt