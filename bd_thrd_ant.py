from collections import deque 
memory = []
deque_store = []
stack_store = []

def show_line(line):
    if len(line) != 0:
        out = '['
        for i in range(len(line)):
            out += str(line[i][0]) + ', '
        out = out[0:len(out)-2]
        out += ']'
        return out
    else:
        return str(line)

while True:
    try:
        print('Введите длину дека: ')
        len1 = int(input())
        print('Введите длину стека: ')
        len2 = int(input())
        print('Введите значения дека: ')
        for i in range(len1):
            inp = int(input())
            node = [inp, i+1]
            deque_store.append(node)
        print('Введите значения стека: ')
        for i in range(len2):
            inp = int(input())
            node = [inp, i + 1]
            stack_store.append(node)
        memory.append(deque_store)
        memory.append(stack_store)
        break
    except ValueError:
        print('Введите правильное число')

menu1 = int(input('Выберите действие: 1 - изменить дек, 2 - изменить стек, 3 - преобразование \n'))
while menu1 != 3:
    if menu1 == 1:
        menu2 = int(input('Выберите действие: 1 - удалить правое, 2 - удалить левое, 3 - просмотр элементов, 4 - добавить справа, 5 - добавить слева, 6 - выход \n'))
        while menu2 != 6:
            if menu2 == 1:
                memory[0].pop()
                print('Последний элемент удален: ' + show_line(memory[0]))
            elif menu2 == 2:
                memory[0].pop(0)
                for i in range(len(memory[0])):
                    memory[0][i][1] = i + 1
                print('Первый элемент удален: ' + show_line(memory[0]))
            elif menu2 == 3:
                print(show_line(memory[0]))
            elif menu2 == 4: 
                print('Введите новый элемент: ')
                inp = int(input())
                node = [inp, len(memory[0]) + 1]
                memory[0].append(node)
                print('Элемент добавлен: ' + show_line(memory[0]))
            elif menu2 == 5: 
                print('Введите новый элемент: ')
                inp = int(input())
                node = [inp, len(memory[0])+1]
                memory[0].insert(0,node)
                print('Элемент добавлен: ' + show_line(memory[0]))
            elif menu2 != 1 and menu2 != 2 and menu2 != 3 and menu2 != 4 and menu2 != 5:
                print('Введите правильное число')
            menu2 = int(input('Выберите действие: 1 - удалить правое, 2 - удалить левое, 3 - просмотр элементов, 4 - добавить справа, 5 - добавить слева, 6 - выход \n'))
        if menu2 == 6:
            menu1 = int(input('Выберите действие: 1 - изменить дек, 2 - изменить стек, 3 - преобразование \n'))
    elif menu1 == 2:
        menu3 = int(input('Выберите действие: 1 - удаление, 2 - просмотр элементов, 3 - добавление, 4 - выход \n'))
        while menu3 != 4:
            if menu3 == 1:
                memory[1].pop()
                print('Последний элемент удален: ' + show_line(memory[1]))
            elif menu3 == 2:
                print(show_line(memory[1]))
            elif menu3 == 3:
                print('Введите новый элемент: ')
                inp = int(input())
                node = [inp, len(memory[1]) + 1]
                memory[1].append(node)
                print('Элемент добавлен: ' + show_line(memory[1]))
            elif menu3 != 1 and menu3 != 2 and menu3 != 3:
                print('Введите правильное число')    
            menu3 = int(input('Выберите действие: 1 - удаление, 2 - просмотр элементов, 3 - добавление, 4 - выход \n'))
        if menu3 == 4:
            menu1 = int(input('Выберите действие: 1 - изменить дек, 2 - изменить стек, 3 - преобразование \n'))
    elif menu1 != 1 and menu1 != 2:
        print('Введите правильное число')
        menu1 = int(input('Выберите действие: 1 - изменить дек, 2 - изменить стек, 3 - преобразование \n'))        

deque_all = []
for i in range(len(deque_store)): 
    deque_all.append(deque_store[i])
for i in range(len(stack_store)): 
    deque_all.append(stack_store[i])
memory.append(deque_all)
print ('преобразовали стек и дек в один дек: ' + show_line(memory[2]))

menu4 = int(input('Выберите действие: 1 - удалить правое, 2 - удалить левое, 3 - просмотр элементов, 4 - добавить справа, 5 - добавить слева, 6 - выход \n'))
while menu4 != 6: 
    if menu4 == 1:
        memory[2].pop()
        print('Последний элемент удален: ' + show_line(memory[2]))
    elif menu4 == 2:
        memory[2].pop(0)
        for i in range(len(memory[2])):
            memory[2][i][1] = i + 1
        print('Первый элемент удален: ' + show_line(memory[2]))    
    elif menu4 == 3:
        print(show_line(memory[2]))
    elif menu4 == 4: 
        print('Введите новый элемент: ')
        inp = int(input())
        node = [inp, len(memory[2]) + 1]
        memory[2].append(node)
        print('Элемент добавлен: ' + show_line(memory[2])) 
    elif menu4 == 5: 
        print('Введите новый элемент: ')
        inp = int(input())
        node = [inp, len(memory[2])+1]
        memory[2].insert(0,node)
        print('Элемент добавлен: ' + show_line(memory[2]))     
    menu4 = int(input('Выберите действие: 1 - удалить правое, 2 - удалить левое, 3 - просмотр элементов, 4 - добавить справа, 5 - добавить слева, 6 - выход \n')) 