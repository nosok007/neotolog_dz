width = 15
length = 50
height = 15
print(width, length, height)
if(width<15 and length<15 and height<15):
    print('Коробка №1')
elif (width > 200 or length > 200 or height > 200):
    print('Упаковка для лыж')
elif(50>width>15 or 50>length>15 or 50>height>15):
    print('Коробка №2')
else:(print('Стандартная коробка №3'))

width = 45
length = 205
height = 45
print(width, length, height)
if(width<15 and length<15 and height<15):
    print('Коробка №1')
elif (length > 200):
    print('Упаковка для лыж')
elif(50>width>15 or 50>length>15 or 50>height>15):
    print('Коробка №2')
else:(print('Стандартная коробка №3'))
