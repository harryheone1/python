# 3 steps to write to a file - truncating
file = open('data/name.txt', 'w')
file.write("Monkey.D.Luffy")
file.close()

# 3 steps to write to another file
file = open('data/name_copy.txt', 'w')
file.write("Monkey.D.Luffy")
file.close()

# 3 steps to read from a file, mode is read by default
file = open('data/name.txt')
print(file.read())
file.close()

# 3 steps to read a file, cursor move with read function argument
file = open('data/name.txt')
print(file.read(3))
print(file.read(6))
file.close()

# 3 steps to read a file, set mode to read explicitly, move cursor to 9 directly
file = open('data/name.txt', 'r')
print(file.read(9))
file.close()

# mode addition and mode write, Escape character of a new line
file = open('data/name_copy.txt', 'a')
file.write("\n")
file.write("Zozoroa Solo")
file.close()
