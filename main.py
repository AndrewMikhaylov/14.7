flag = True
isNumber = True
runtimeTimes = 0
typeTimes = 0
valueTimes = 0
while flag:
    print("Введіть число")
    number = input()
    try:
        int(number)
    except ValueError:
        isNumber = False
    if(number == "досить"):
        flag=False
        continue
    if not isNumber:
        print("Програма приймає на вхід тільки числа та команду про зупинку")
        continue
    try:
        if int(number)>9:
            raise RuntimeError("Число більше за 9")
        if int(number)<0:
            raise TypeError("Число менше за 0")
        if int(number)<=9 and int(number)>=0:
            raise ValueError("Число більше за 0 та менше за 9")
    except RuntimeError:
        print("RuntimeError: Число більше за 9")
        runtimeTimes= runtimeTimes+1
    except TypeError:
        print("TypeError: Число менше за 0")
        typeTimes = typeTimes+1
    except ValueError:
        print("ValueError: Число більше за 0 та менше за 9")
        valueTimes = valueTimes+1

print("Кількість RuntimeError:")
print(runtimeTimes)
print("Кількість TypeError:")
print(typeTimes)
print("Кількість ValueError:")
print(valueTimes)