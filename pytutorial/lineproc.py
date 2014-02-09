
f_in = open('data/ZenOfPython.txt')
for line in f_in.readlines():
    words = line.split(' ')
    print words[0]

f_in.close()
