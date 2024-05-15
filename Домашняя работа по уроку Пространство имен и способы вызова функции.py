def test ():
    a = 10
    b = 20
    print(a, b)

def test_2 (*, c = 15, d = 30, e =45):
    print (c, d, e)

def test_3 (c = 15, d = 30, e =45):
    print (c, d, e)

def test_4 (c, d, e):
    print (c, d, e)


test()
test_2()
test_3()
test_4(150, 250, 350)