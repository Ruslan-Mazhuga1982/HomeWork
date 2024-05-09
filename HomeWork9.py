# for i in 1, 2, 3, 4:
#     print(i)
# list_ = ['one', 'two', 'three']
# for i in list_:
#     print(i)
#
#
# list_ = ['one', 'two', 'three']
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
#
# print(list_)
#
# list_ = ['one', 'two', 'three']
# for i in range (5):
#     print(i)
#
#
# #print(list_)
#
# list_ = ['one', 'two', 'three']
# for i in range (len(list_)):
#     list_[i] = ' (: '
#     #print(list_[0])
#     #print(list_[1])
#     #print(list_[2])
#     #print(list_[0:3:])
#     print(list_)
#
#
#
#
# #print(list_)
#
# list_ = ['one', 'two', 'three']
# for i in range (len(list_)):
#     list_[i] = ' :( '
#
# print(list_)
#
# list_ = ['one', 'two', 'three']
# list_2 = [2, 3, 4, 5, 1]
# sum_ = 0
# for i in range(len(list_2)):
#     sum_ += list_2[i]
#
# print(sum_)
# a = 10
# for i in range(1, 200):  # start, stop, step
#     for j in range(1, 200):
#         for k in range(1,200):
#             print(f'({i} * {j}) * {k} = {(i * j) * k}')
#         #print(f'{i} + {j} = {i + j}')
#
#
# cars_count_ = 0
# cars_ = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
# for i in cars_:
#     print('Я езжу на автомобиле марки', i)
# for j in range(1, 11):
#     print(f'{i} * {j} * 10 = {i * j}')
#cars_count_ = 0
cars_ = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
cars_count = 0
for i in cars_:
    print('Я езжу на автомобиле марки', i, cars_count)
    cars_count += 10
#Вариант 2
cars_ = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']
cars_count = 0
for i in range(10):
    i = cars_[0]
    print('Я езжу на автомобиле марки', i, cars_count)
    cars_count += 10

