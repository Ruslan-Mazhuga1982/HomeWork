def print_params(name):
    print('Hello', name)
parametr_1 = 25
parametr_2 = 30
parametr = parametr_1 * parametr_2
dannie = 36
def print_params(parametr):
    print('Hello', parametr, parametr_1, parametr_2)
def spisok(dannie):
    print(dannie)

print_params('Ruslan')
print_params('Ruslan')

for i in range (3):
    print_params(parametr)

spisok(dannie)