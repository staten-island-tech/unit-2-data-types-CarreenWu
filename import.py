""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" temp = 50
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" x=13
if 0 == x%2:
    print('even')
else:
    print('odd') """

""" bill=25
service=input('how was the meal?')
if service == 'great' :
    bill=bill*.25
    print(bill)
elif service == "good" :
    bill=bill*.20
    print(bill)
elif service == 'okay' :
    bill=bill*.15
    print(bill)
elif service == 'bad' :
    bill=bill*0
    print(bill) """

""" string = input("give me a sentence. ")
words = string.split()
count=0
for i in words:
    count=count+1
    print(count)  """

""" num=int(input('give me a number. '))
def factor(x):
    print(f'factors of [x] are...')
    for i in range(1, x + 1):
        if x%i == 0:
            print(i)
factor(num) """

num=int(input('give me a number '))
number=int(input('give me another number '))
def gcf(x,y):
    greatest_common_factor=1
    for i in range (1, min(y,x)+1):
        if x%i == 0 and y%i==0:
            greatest_common_factor=i
    return greatest_common_factor
result = gcf(num,number)
print(f"the of gcf(num) and(number) is: {result}")