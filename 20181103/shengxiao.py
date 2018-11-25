#file1 = open('xy.txt','w')
#file1.write('5 chingyang')
#file1.close()

#file1 = open('xy.txt')
#print(file1.read())

# file1 = open('xy.txt')
# for line in file1.readlines():
#     print(line)
#     print('-------------------')
# print(file1.tell())
# file1.read(1)

# file1 = open('xy.txt','a')
# file1.seek(0)
# file1.write('0 randyxu\n')
# file1.close()
# file1 = open('xy.txt')
# for line in file1.readlines():
#     print(line)
#     print('-------------------')
# print(file1.tell())

# print(file1.tell())
file = open('xy.txt','a')
file1.seek(5,0)
file1.write('a billnisrui')
file1.close()



