# № 1
tst = 123
txt1 = str(tst)[0]
txt2 = str(tst)[1]
txt3 = str(tst)[2]
res =  int(txt1) + int(txt2) + int(txt3)
print(res)
del tst, txt1, txt2, txt3, res

# № 2
tst = 4567
txt1 = str(tst)[0]
txt2 = str(tst)[1]
txt3 = str(tst)[-1]
res =  (int(txt1) + int(txt2)) - int(txt3)
print(res)
del tst, txt1, txt2, txt3, res
