def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


    inner_function() # Не будет работать так она находиться в локальном пространстве имен
####################### Вариант 2
def test_function_1():
    def inner_function_1():
        print('Я в области видимости функции test_function_1')
    inner_function_1()


    inner_function_1() # Не будет работать так она находиться в локальном пространстве имен
test_function_1()