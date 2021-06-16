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

# largest so far
lnum = -1
print('before lnum was: ', lnum)
for i in [3, 15, 9, 74, 43, 12] :
    if i > lnum:
        lnum = i
    print(lnum, i)
print('after lnum is: ', lnum)

# smallest so far
snum = 75
print('before smallest num was: ', snum)
for inum in [2, 59, 31, 88, 29, 99, 14, 8] :
    if inum < snum:
        snum = inum
    print (snum, inum)
print('after smallest num is: ', snum)

# 05-01 EX Python For Everybody Course
# Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.
num = 0
tot = 0.0
while True:
    x = input('Enter a number: ')
    if x == 'done':
        break
    try:
        x = float(x)
    except:
        print('Wrong number, asshole. Try again.')
        continue
    num = num + 1
    tot = tot + x  
av = tot/num
print('Total is:', tot,'.','Average is:', av,'.')

