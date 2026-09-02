# № 1
num1 = 1
num2 = 2
res =  str(num1) +  str(num2)
print(res)
del num1, num2, res

# № 2
tst1 = 'abc'
txt2 = 123
res = tst1 + str(txt2)
print(res)
del tst1, txt2, res

# № 3
tst = 123
txt = str(tst)
res = len(txt)
print(res)
del txt, tst, res

# № 4 Как решить это иначе, если не заходить по темам вперед?
tst = 456
txt = str(tst)
res = int(txt[0]) + int(txt[1]) + int(txt[2])
print(res)
del txt, tst, res