def bubble_sort(nums):  #Пузырьковый метод сортировки
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):  
            if nums[i] > nums[i + 1]: 
                nums[i], nums[i + 1] = nums[i + 1], nums[i] 
                swapped = True

def maxmin_sort(nums): #Сортировка макс/мин
    '''for i in range(len(nums) - 1):
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j = j + 1
        nums[i], nums[m] = nums[m], nums[i]'''
    for i in range(len(nums)): 
        minimum = i       
        for j in range(i + 1, len(nums)): 
            if nums[j] < nums[minimum]:
                minimum = j
        nums[minimum], nums[i] = nums[i], nums[minimum]  

def insertion_sort(nums):  #сортировка вставкой
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert      

print('Выбор метода сортировки: пузырьком - 1, мак\мин - 2, вставка - 3, выход - 4')
chs = int(input("Выбор: "))
while chs != 4:
    if chs == 1:
        random_list_of_nums = [5, 2, 1, 8, 4]  
        bubble_sort(random_list_of_nums)  
        print(random_list_of_nums)
    if chs == 2:
        random_list_of_nums = [7, 5, 19, 23, 4]
        maxmin_sort(random_list_of_nums)
        print(random_list_of_nums)
    if chs == 3:
        random_list_of_nums = [9, 1, 15, 28, 6]  
        insertion_sort(random_list_of_nums)  
        print(random_list_of_nums)
    chs = int(input("Выбор: "))

