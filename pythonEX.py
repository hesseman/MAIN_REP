# 03-01 EX Python For Everybody Course
# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

x = float(input('Enter hours: '))
y = float(input('Enter rate: '))
if x >= 40:
    pay = (x - 40.0) * (y * 0.5)  
    op = pay + (x * y)
    print('Pay: ',op)
elif x < 40:
    pay = x * y
    print('Pay: ',pay)

# 03-02 EX Python For Everybody Course
# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

x = input('Enter hours: ')
y = input('Enter rate: ')

def normal():
    if x >= 40:
        pay = (x - 40.0) * (y * 0.5)  
        op = pay + (x * y)
        print('Pay: ',float(op))
    elif x < 40:
        pay = x * y
        print('Pay: ',float(pay))
try:
    x = float(x)
    y = float(y)
except:
    x = -1
    y = -1
    
if x == -1 or y == -1:
    print('Error, try again.')
else:
    normal()
