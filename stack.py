#Initialize 3 stack
stack_1 = []
stack_2 = []
stack_3 = []

i = int(input('Count of numbers for stack_1: \n')) #add numbers in first stack
for a in range(i):
    stack_1 += input()
print(stack_1)

i = int(input('Count of numbers for stack_2: \n')) #add numbers in second stack 
for a in range(i):
    stack_2 += input()
print(stack_2)

i = int(input('Count of numbers for stack_3: \n')) #add numbers in third stack
for a in range(i):
    stack_3 += input()
print(stack_3)

stack_all = [] #initialize big stack
for i in range(len(stack_1)): #add numbers from firts to big
    stack_all += stack_1[i]
for i in range(len(stack_2)): #add numbers from second to big 
    stack_all += stack_2[i]
for i in range(len(stack_3)): #add numbers from third to big
    stack_all += stack_3[i]
print(stack_all) #print big stack

menu = int(input('What u gonna do? 1 - pop, 2 - index, 3 - add, 4 - change prev stack, 5 - update all stack, 6 - exit \n')) #make an menu
while menu != 6: #stop for menu
    if menu == 1:
        stack_all.pop() #deleting last item in stack
        print(stack_all)
    elif menu == 2:
        ind = int(input('Enter index: \n')) #find an stack member
        print(stack_all[ind])
    elif menu == 3: #add last item in stack
        cou = input('Enter: \n')
        stack_all += cou
        print(stack_all)
    elif menu == 4:
        menu_ch = int(input('What u gonna do? 1 - pop, 2 - index, 3 - add\n'))
        if menu_ch == 1:
            menu_st = int(input('Choose stack: 1, 2, 3?'))
            if menu_st == 1:
                stack_1.pop() #deleting last item in stack
                print(stack_1)
            elif menu_st == 2:
                stack_2.pop() #deleting last item in stack
                print(stack_2)
            elif menu_st == 3:
                stack_3.pop() #deleting last item in stack
                print(stack_3)
            else:
                continue
        elif menu_ch == 2:
            menu_st = int(input('Choose stack: 1, 2, 3? \n'))
            if menu_st == 1:
                ind = int(input('Enter index: \n')) #find an stack member
                print(stack_1[ind])
            elif menu_st == 2:
                ind = int(input('Enter index: \n')) #find an stack member
                print(stack_2[ind])
            elif menu_st == 3:
                ind = int(input('Enter index: \n')) #find an stack member
                print(stack_3[ind])
            else:
                continue
        elif menu_ch == 3:
            menu_st = int(input('Choose stack: 1, 2, 3?'))
            if menu_st == 1: #add last item in stack
                cou = int(input('Enter: \n'))
                stack_1 += cou
                print(stack_1)
            elif menu_st == 2: #add last item in stack
                cou = int(input('Enter: \n'))
                stack_2 += cou
                print(stack_2)
            elif menu_st == 3: #add last item in stack
                cou = int(input('Enter: \n'))
                stack_3 += cou
                print(stack_3)
            else:
                continue
    elif menu == 5:
        stack_all.clear()
        for i in range(len(stack_1)): #add numbers from firts to big
            stack_all += stack_1[i]
        for i in range(len(stack_2)): #add numbers from second to big 
            stack_all += stack_2[i]
        for i in range(len(stack_3)): #add numbers from third to big
            stack_all += stack_3[i]
        print(stack_all) #print big stack
    menu = int(input('What u gonna do? 1 - pop, 2 - index, 3 - add, 4 - change prev stack, 5 - update all stack, 6 - exit \n')) #start menu again3