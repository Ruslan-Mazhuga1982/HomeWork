def print_params(a = 1, b = 'строка', c = True):

    if c == 25:
        c = True
    else:
        c = False

    print (a,b,c)

    print()
################# Вызов функции с разным количеством аргументов, включая вызов без аргументов.
print_params()
print_params(25,'Hello',30)
print_params(70, '21212', 25)
print_params((10+13),"prikol",25)
################# Вызов функции  print_params с (b = 25) print_params(c = [1,2,3]).

def print_params_1(a = 1, b = 'строка', c = True):

    print(a,b,c)


print_params_1(1, 25, True)
print_params_1(1,b = 25, c = [1,2,3])

def print_params_2(a = 1, b = 'строка', c = True):
    print(a,b,c)
values_list = [15, ('Я кортеж ! Меня нельзя изменить!!!'), 'Я str и меня можно изменить']
values_dict = {'Max': 12345, 'Egor': 123456, 'Alex': 654321}
values_list_2 = [10,20,30]


print_params_2(values_list,'25123', True)
#print_params_2(*values_list,'25123', True) # Не будет работать так как при распаовке
                                            # передается больше значений чем присвоено функци
print_params_2(values_list, values_dict,True)
# print_params_2(*values_list_2, 42)# Не будет работать так как при распаовке
                                    # передается больше значений чем присвоено функци
def print_params_3(**kwargs):
    print(kwargs)
    values_dict = {'Max': 12345, 'Egor': 123456, 'Alex': 654321}
    for key, value in kwargs.items():
        print(key, value)

print_params_3(**values_dict)

