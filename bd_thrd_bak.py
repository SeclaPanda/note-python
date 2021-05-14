stack_1 = []
stack_2 = []
stack_3 = []
memory = []

len_1 = int(input('len stack 1: '))
len_2 = int(input('len stack 2: '))
len_3 = int(input('len stack 3: '))

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

print('Enter data to stack 1: ')
for i in range(len_1):
    inp = int(input())
    node = [inp, i + 1]
    stack_1.append(node)
memory.append(stack_1)

print('Enter data to stack 2: ')
for i in range(len_2):
    inp = int(input())
    node = [inp, i + 1]
    stack_2.append(node)
memory.append(stack_2)

print('Enter data to stack 3: ')
for i in range(len_3):
    inp = int(input())
    node = [inp, i + 1]
    stack_3.append(node)
memory.append(stack_3)

deque_all = []
for i in range(len(stack_1)): 
    deque_all.append(stack_1[i])
memory.append(deque_all)

for i in range(len(stack_2)): 
    deque_all.append(stack_2[i])
memory.append(deque_all)

for i in range(len(stack_3)): 
    deque_all.append(stack_3[i])
memory.append(deque_all)

print ('Make 1 stack from 3 stack: ' + show_line(memory[3]))

menu = int(input('Menu. 1 - show, 2 - add, 3 - pop, 4 - exit. Chs: '))
while menu != 4:
    if menu == 1:
        print(show_line(memory[3]))
    elif menu == 2:
        print('Введите новый элемент: ')
        inp = int(input())
        node = [inp, len(memory[3]) + 1]
        memory[3].append(node)
        print('Элемент добавлен: ' + show_line(memory[3]))
    elif menu == 3:
        memory[3].pop()
        print('last element poped: ' + show_line(memory[3]))
    menu = int(input('Menu. 1 - show, 2 - add, 3 - pop, 4 - exit. Chs: '))