# Напишите программу, которой на вход подается последовательность чисел через пробел, - ОК   1 2 4 22 7 66 3 14 24 75 43
# а также запрашивается у пользователя любое число.- ОК
# (В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных).
# Далее программа работает по следующему алгоритму:
# -Преобразование введённой последовательности в список -ОК
# -Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию) - OK
# -Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле.
# Реализуйте его также отдельной функцией.
# Подсказка: Помните, что у вас есть числа, которые могут не соответствовать заданному условию.
# В этом случае необходимо вывести соответствующее сообщение


i = 0
while i < 1:
    try:
        numb_list = input('введите ряд любых чисел через пробел: ').split()
        len_list = numb_list
        numb_list = map(float, numb_list)
        list_list = list(numb_list)
        # print('numb_list :',list_list)

        if len(len_list) < 2:
            print ('введите не менее 2 элементов')
            print()
        else:
            i += 1
    except ValueError:
        print("НЕ правильный ввод, принимаются ТОЛЬКО числа ")
        print()
i = 0
while i<1:

    try:
        other_number = input("Введите ещё одно любое число - ")
        other_number = float(other_number)
        if other_number != float(other_number):
            print()
        else:
            i += 1
    except:
        print("НЕ правильный ввод. принмается только число")

print('Список:', list_list)
sort_list = sorted(list_list)
print('Сортированный список:', sort_list)

end = len_list
array = sort_list
element = other_number

def binary_search(array, element, start, end):
    if start > end:
        return False

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search(array, element, start, mid-1)
    else:
        return binary_search(array, element, mid+1, end)


id_elem = binary_search(array, element, 0, len(array))
if id_elem != 0:
    id_left = id_elem - 1
    print('номер ID элемента, который ЛЕВЕЕ введенного числа-', id_left)
    id_right = id_elem + 1
    print('номер ID элемента, который ПРАВЕЕ введенного числа-', id_right)
else:
    print('нет ID  числа в списке !')