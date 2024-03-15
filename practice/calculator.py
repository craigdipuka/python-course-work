#this is a simple calculator program for practice


#asking user which function they want to perform
funct = int(input(" Select what fuction you want : \n1-Addition  2-Subtraction  3-Division  4-Modulus\n"))

match funct: 
    case 1: 
        numb1 = int (input("Please enter X: "))
        numb2 = int (input("Please enter Y: "))
        math = numb1+numb2
        print(f"{numb1} + {numb2} = {math}")
    
    case 2:
        numb1 = int (input("Please enter X: "))
        numb2 = int (input("Please enter Y: "))
        math = numb1-numb2
        print(f"{numb1} - {numb2} = {math}")

    case 3:
        numb1 = int (input("Please enter X: "))
        numb2 = int (input("Please enter Y: "))
        math = numb1/numb2
        print(f"{numb1} / {numb2} = {math}")
    
    case 3:
        numb1 = int (input("Please enter X: "))
        numb2 = int (input("Please enter Y: "))
        math = numb1%numb2
        print(f"{numb1} % {numb2} = {math}")
    

    
    

