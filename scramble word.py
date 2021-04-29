# word = c for c in word
'''
if open('words.txt'):
    print('working')
else: 
    print('no file in the directory. Please create a .txt file called "words" ')
'''
import random
output = {}
print('this will only work if you have created a .txt file')
filename = input("what is your file called? (without the .txt) ")
input('if you havent made this yet make it before continuing (press enter to continue) ')
file = open(filename+'.txt').read()
print('opened')
words = file.split(',')
for i in words:
    quinty = list(i)
    ronta = ""
    random.shuffle(quinty)
    for d in quinty:
        ronta = ronta + d
    output[i] = ronta
password = input("what do you want the file to be called? ")
file = open(password+".txt", "w") 
file.write(str(output)) 
file.close() 
