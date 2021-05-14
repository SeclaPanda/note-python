#Initialize 3 stack
stack_1 = []
stack_2 = []
stack_3 = []

i = int(input('Count of numbers for stack_1: \n')) #add numbers in first stack
for a in range(i):
    stack_1.append(input())
print(stack_1)

i = int(input('Count of numbers for stack_2: \n')) #add numbers in second stack 
for a in range(i):
    stack_2.append(input())
print(stack_2)

i = int(input('Count of numbers for stack_3: \n')) #add numbers in third stack
for a in range(i):
    stack_3.append(input())
print(stack_3)

stack_all = [] #initialize big stack
for i in range(len(stack_1)): #add numbers from firts to big
    stack_all.append(stack_1[i])
for i in range(len(stack_2)): #add numbers from second to big 
    stack_all.append(stack_2[i])
for i in range(len(stack_3)): #add numbers from third to big
    stack_all.append(stack_3[i])
print(stack_all) #print big stack

menu = int(input('What u gonna do? 1 - pop, 2 - index, 3 - add, 4 - exit \n')) #make an menu
while menu != 4: #stop for menu
    if menu == 1:
        stack_all.pop() #deleting last item in stack
        print(stack_all)
    elif menu == 2:
        ind = int(input('Enter index: \n')) #find an stack member
        print(stack_all[ind])
    elif menu == 3: #add last item in stack
        cou = int(input('Enter: \n'))
        stack_all.append(cou)
        print(stack_all)
    menu = int(input('What u gonna do? 1 - pop, 2 - index, 3 - add, 4 - exit \n')) #start menu again