def PowerWithModules(number,power,dividend):
    number=number%dividend
    result=1
    for i in range(power):
        result=number*result
    return result%power
    
    
number=int(input("enter the number: "))
power=int(input("enter the power: "))
dividend=int(input("enter the dividend: "))
print(PowerWithModules(number,power,dividend))