#meow
import math
import sys
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"



def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def divide(x, y):
    return x / y
def times(x, y):
    return x * y


while True:
    print("-------------------------------------------")
    print("1. addition")
    print("-------------------------------------------")
    print("2. subtraction")
    print("-------------------------------------------")
    print("3. multiply")
    print("-------------------------------------------")
    print("4. division")
    print("-------------------------------------------")
    print("5. ★ check armstrong numbers ★")
    print("-------------------------------------------")

    choice = input("option 1/2/3/4/5 = ")

    if choice in ('1', '2', '3', '4',):
        first = True
        second = True
        while (first):
            try:
                v = float(input('first number = '))
                #c = float(input('second number = '))
                #vc = False
                first = False
            except ValueError:

                sys.stdout.write(RED)
                print("enter number idiot lol ")
                sys.stdout.write(RESET)
                continue

        while (second):
            try:
                c = float(input('second number = '))
                second = False
            except ValueError:

                sys.stdout.write(RED)
                print("enter number idiot lol ")
                sys.stdout.write(RESET)
                continue

        if choice == '1':
            print("-------------------------------------------")

            sys.stdout.write(GREEN)
            print (v, "+", c, "=", plus(v, c))
            sys.stdout.write(RESET)

        elif choice == '2':
            print("-------------------------------------------")

            sys.stdout.write(GREEN)
            print (v, "-", c, "=", minus(v, c))
            sys.stdout.write(RESET)

        elif choice == '3':
            print("-------------------------------------------")

            sys.stdout.write(GREEN)
            print (v, "*", c, "=", times(v, c))
            sys.stdout.write(RESET)

        elif choice == '4':
            print("-------------------------------------------")

            sys.stdout.write(GREEN)
            print(v, "/", c, "=", divide(v, c))
            sys.stdout.write(RESET)

    if choice in ('5'):
        poop = True
        while poop:
            try:
                num = int(input('number = '))
                poop = False
            except ValueError:
                    sys.stdout.write(RED)
                    print("enter number idiot lol ")
                    sys.stdout.write(RESET)
                    continue

        if choice =='5':
            print("-------------------------------------------")
            sys.stdout.write(GREEN)
            #all the variables needed
            digits = len(str(num))
            sum = 0
            extra = list()
            temp = num
            xd = extra
            g = len(str(num))
            #equation


            if digits == 3:
                while temp > 0:
                    digit = temp % 10
                    extra.append(digit)
                    sum += digit ** g
                    temp //= 10
                print (xd[2],"³",xd[1],"³",xd[0],"³", "=", sum)
                if sum == num:
                    print(num,"is an armstrong number")
                    sys.stdout.write(RESET)
                else:
                    sys.stdout.write(RED)
                    print(num,"is not an armstrong number")
                    sys.stdout.write(RESET)

            if digits == 4:
                while temp > 0:
                    digit = temp % 10
                    extra.append(digit)
                    sum += digit ** g
                    temp //= 10
                print (xd[3],"³",xd[2],"³",xd[1],"³",xd[0],"³", "=", sum)
                if sum == num:
                    print(num,"is an armstrong number")
                    sys.stdout.write(RESET)
                else:
                    sys.stdout.write(RED)
                    print(num,"is not an armstrong number")
                    sys.stdout.write(RESET)

            if digits == 5:
                while temp > 0:
                    digit = temp % 10
                    extra.append(digit)
                    sum += digit ** g
                    temp //= 10
                print (xd[4],"³",xd[3],"³",xd[2],"³",xd[1],"³",xd[0],"³", "=", sum)
                if sum == num:
                    print(num,"is an armstrong number")
                    sys.stdout.write(RESET)
                else:
                    sys.stdout.write(RED)
                    print(num,"is not an armstrong number")
                    sys.stdout.write(RESET)

            if digits == 6:
                while temp > 0:
                    digit = temp % 10
                    extra.append(digit)
                    sum += digit ** g
                    temp //= 10
                print (xd[5],"³",xd[4],"³",xd[3],"³",xd[2],"³",xd[1],"³",xd[0],"³", "=", sum)
                if sum == num:
                    print(num,"is an armstrong number")
                    sys.stdout.write(RESET)
                else:
                    sys.stdout.write(RED)
                    print(num,"is not an armstrong number")
                    sys.stdout.write(RESET)

            if digits == 7:
                while temp > 0:
                    digit = temp % 10
                    extra.append(digit)
                    sum += digit ** g
                    temp //= 10
                print (xd[6],"³",xd[5],"³",xd[4],"³",xd[3],"³",xd[2],"³",xd[1],"³",xd[0],"³", "=", sum)
                if sum == num:
                    print(num,"is an armstrong number")
                    sys.stdout.write(RESET)
                else:
                    sys.stdout.write(RED)
                    print(num,"is not an armstrong number")
                    sys.stdout.write(RESET)


    else:

        sys.stdout.write(RED)
        print ("something went wrong, yikes")
        print ("ERROR: r u ok? lol")
        import webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0%22")
        sys.stdout.write(RESET)