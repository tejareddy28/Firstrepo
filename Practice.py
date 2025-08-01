#if 5>2:
#   print("Greater than") #indentation refers to spaces before the code to identify a block of code

# Input/Output Basics

#username = input() # input - flexibity to take input as string from user.
#print(username) #input() = Sanju Reddy

'''sport="Football"
print(len(sport))
print(sport[len(sport)])'''

'''a=input()
b=input()
print(a+b)'''

#Type cpnversions
'''
a=10.5
a=int(a)
print(a)

a="10"
b="*"*int(a)
print(b)

print(type(True))'''

'''slogan = "Save Earth, Save Lives"
length = len(slogan)

for i in range(length):
    if slogan[i] == " ":
        print(slogan[:i])'''

num1 = 10
num2 = 20
total = 0
for i in range(num1,num2):
    if(i % 5 == 0):
        total = total+i

print(total)

  
