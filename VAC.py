print("Creating Functions")

def Moduler(x,y):
    print(x%y)

print("Moduler Divition")
Moduler(105,2)
print("------------------------")
print("Iterables :")
x = [1,2,3,4,5,6,7,8]
for i in x:
    print(i*2,end=" ")
for j in x:
    print(j)
print("------------------------")
print(" Conditional Statements :")
x=1
while x<5:
    print(x)
    x+=1
print("------------------------")
print("If Conditional Statements :")
x = int(input("Enter a number : "))
if x == 1:
    print("You entered 1")
else :
    print("You entered a number other than 1 which is :",x)
print("------------------------")
def calculator(x,y,op=" "):
    if op == "+":
        print(x+y)
    elif op == "-":
        print(x-y)
    elif op == "*":
        print(x*y)
    elif op == "/":
        print(x/y)
    else:
        print("Invalid Operator")

x=int(input("Enter first number : "))
y=int(input("Enter second number : "))
operator=input("Enter operator (+,-,*,/) : ")
calculator(x,y,operator)