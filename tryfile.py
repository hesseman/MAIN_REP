infile = input('Type file name: ')
try:
    ofile = open(infile)
except:
    print('This: ', infile,'is a wrong file name. Try again')
    quit()

count = 0
onfile = open(infile)
for cheese in onfile:
    count = count + 1

onfile = open(infile)
rfile = onfile.read()
chnum = len(rfile)

print('Number of lines: ', count)
print('Number of characters: ', chnum)
