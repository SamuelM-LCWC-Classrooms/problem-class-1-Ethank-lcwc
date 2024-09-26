def task_1():
    total_resistance = 0
    measurements = []
    user = int(input("how many values would you like to enter\n"))
    for i in range(user):
        i = int(input("what value is the resistor\n"))
        total_resistance += i
        measurements.append(i)

    return total_resistance

def task_2(cost):
    cost = float(cost)
    tipc = False
    while tipc == False:
        tip = float(input("what percentage tipped\n"))
        if tip < 0.01:
            print("incorrect please try again")
            tipc = False
        else:
            tipc = True
    tip = tip / 100
    tip *= cost
    VAT = (tip + cost) * 0.2
    total_cost = cost + tip + VAT
    
    return total_cost

def task_3():
    result = []
  
    usera = False
    while usera == False:
        user = int(input("what number would you like to append too\n")) + 1
        if user < 0:
            print("please enter a number above 0")
            usera = False
        else:
            usera = True

    for i in range(1,user):
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
            result.append(i)
        elif i % 3 == 0:
            i = "Buzz"
            result.append(i)
        elif i % 5 == 0:
            i = "Fizz"
            result.append(i)
        else:
            result.append(i)

        

    return result

def task_4():
    result = []
    ans = False
    while ans == False:
        user = int(input("enter a value for n \n"))
        if user < 0:
            print("please enter an integer greater than 0 ")
            ans = False
        else:
            result.append(user)
            ans = True
    while user != 1:
        if user % 2 == 0:
            user = user / 2
            result.append(user)
        else:
            user = (user * 3) + 1
            result.append(user)

    return result

def task_5():
    height = 0
    row_ammount = 1
    stop = False
    ans = False
    while ans == False:
        user = int(input("how many blocks do u have \n"))
        if user < 0:
            print("please enter an integer greater than 0 ")
            ans = False
        else:
            ans = True
    
    while user > 0:
        user -= row_ammount
        if user < 0:
            return height
        
        else:
            row_ammount += 1
            height += 1

    return height

