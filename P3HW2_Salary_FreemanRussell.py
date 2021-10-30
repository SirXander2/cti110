
#CTI-110
#P3HW2 - Salary
#Russell Freeman
#10/29/2021
# This program takes user input employee, hour worked and pay rate then outputs regular pay, overtime pay, gross pay.
def main():

    employee_name = input('Enter employee\'s name: ')
    hours_worked = int(input('Enter number of hours worked: '))
    pay_rate = float(input('Enter employee\'s pay rate: '))
    main()    


# User input to define employee name,hours and pay



employee_name = input('Enter employee\'s name: ')
hours_worked = int(input('Enter number of hours worked: '))
pay_rate = float(input('Enter employee\'s pay rate: '))
print('-----------------------------------------------------------------------')
print ('Employee name: ', employee_name)
print()

# Calculate if overtime hours
if hours_worked != 40:
    overtime = (hours_worked - 40)
# Calculate overtime pay for time and half
overtime_pay = ((pay_rate / 2 + pay_rate) * overtime)
# Calculate regular hour pay from user input
regular_pay = (pay_rate * 40)
# Calculate gross pay 
gross_pay = (regular_pay + overtime_pay)

print ('Hours Worked   ','Pay Rate   ','OverTime   ','OverTime Pay   ', 'RegHour Pay   ',' Gross Pay',)
print ('------------------------------------------------------------------------------------------------')
print ('{:.1f}'.format(hours_worked),('          '),pay_rate,('       '),'{:.1f}'.format(overtime),('      '),overtime_pay,('         '),'${:.2f}'.format(regular_pay),('       '),'${:.2f}'.format(gross_pay))  




