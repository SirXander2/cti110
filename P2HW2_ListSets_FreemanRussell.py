#CTI-110
#P2HW2 - List and Sets
#Russell Freeman
#10/15/2021

#user input numbers
num1 = float(input('Enter num 1: '))
num2 = float(input('Enter num 2: '))
num3 = float(input('Enter num 3: '))
num4 = float(input('Enter num 4: '))
num5 = float(input('Enter num 5: '))
num6 = float(input('Enter num 6: '))


created_list = [ num1, num2, num3, num4, num5, num6 ]
print ('\nCreated List')
print(created_list)


small_num = min(created_list)
large_num = max(created_list)
sum_nums = sum(created_list)


print('Smallest number in List:', small_num ) 
print('Largest number in List:' , large_num )
print('Sum of numbers in List:' , sum_nums ) 
print('Average of numbers in List:' , sum_nums / 6 ) 


num_set = set(created_list)
print('\nCreated set')
print(num_set)
