#Python Homework - calculate cost
#10/15/2021
#CTI-110 P2HW1 - Miles Per Gallon
#Russell Freeman


miles_driven = int(input('Enter Miles Driven: '))


gallons_used = int(input('Enter Gallons Used: '))                


cost_pergallon = float(input('Enter Cost Per Gallon: '))                

                
#calculate gallons used
miles_pergallon = miles_driven / gallons_used                  
print('\nMiles Per Gallon:  ', ('{0:.2f}'.format(miles_pergallon )))

#calculate total gas cost
total_gascost = cost_pergallon * gallons_used                   
print('Total Gas Cost:    ',('${0:.2f}'.format(total_gascost )))


#calculate cost per mile
cost_permile = total_gascost / miles_driven 
print('Cost Per Mile:     ', ('${0:.1f}'.format(cost_permile )))
                                                
