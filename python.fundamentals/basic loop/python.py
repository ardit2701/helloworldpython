for i in range(151):
    print(i)
for i in range(5, 1001, 5):
    print(i)
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
sum_odd = 0
for i in range(1, 500001, 2):  
    sum_odd += i

print("The sum of odd integers from 0 to 500,000 is:", sum_odd)
for number in range(2018, -1, -4):
    print(number)
lowNum = 2
highNum = 9
mult = 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)