# read each line and print
file = open('data/one_piece_charactor.txt', 'r')
print(file.readline())  # read one line
print('index move one time to %i', file.tell())
for line in file.readlines():
    print(line)
    print('index move after for loop is %i', file.tell())
    print('========')
file.close()

# find the current index of cursor
# move back to start of the file
file2 = open('data/one_piece_charactor.txt', 'r')
step1 = 3
file2.read(step1)
print('index after moving step %i is %i' % (step1, file2.tell()))
step2 = 5
file2.read(step2)
print('index after moving step %i is %i' % (step2, file2.tell()))
file2.seek(0)
print('index after seek operation is %i' % (file2.tell()))
file.close()

try:
    file3 = open('data/one_piece_charactor1.txt', 'r')
except FileNotFoundError:
    print('file is not there')
finally:
    print('enter the finally block')

file4 = open('data/one_piece_charactor.txt', 'r')
try:
    for line in file.readlines():
        print(line)
        a_file = None
        s = a_file.name
except Exception:
    print('error in program')
finally:
    print('enter the finally block and ready to close')
    file4.close()

