number = 123456
x1 = number//1000
x2 = number%1000
sumX1 = sum(map(int, str(x1)))
sumX2 = sum(map(int, str(x2)))
print(sumX1, sumX2)
print(x1, x2)
if(sumX1 != sumX2):
    print('билет несчастливый((((')

number = 123321
x1 = number//1000
x2 = number%1000
sumX1 = sum(map(int, str(x1)))
sumX2 = sum(map(int, str(x2)))
print(sumX1, sumX2)
print(x1, x2)
if(sumX1 == sumX2):
    print('билет счастливый)))')