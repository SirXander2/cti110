highway_number = int(input())

if ((highway_number < 1) or (highway_number > 999) or ((highway_number % 100) == 0)): # Invalid

    print('{} is not a valid interstate highway number.'.format(highway_number))

else:
    if highway_number >99:
        primary = highway_number % 100
        print('I-',highway_number,' is auxiliary, serving I-',primary,',', sep='',end='')

    else:
        print('I-',highway_number, ' is primary,', sep='', end='')
    if highway_number %2==0:
        print(' going east/west.' )
    else:
        print(' going north/south.')
   