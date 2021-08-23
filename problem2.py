'''Q1 -> Calculate the factorial of a given number.
   Q2 -> Find the number of trailing zeroes in that factorial.'''

def factorial(n):
    f = 1
    if n != 1:
        for i in range(n + 1):
            if i != 0:
                f *= i
        return f
    else:
        return f

def trailingZeroesInFactorial(n):
    numOfTens = 0
    numOfTwos = 0
    numOfives = 0
    if n != 1 or n != 0:
        for i in range(n + 1):
            if i != 0:
                while True:
                    if i % 5 == 0:
                        i = i/5
                        numOfives += 1
                        continue
                    elif i % 2 == 0:
                        i = i/2
                        numOfTwos += 1
                        continue
                    else:
                        break
        numOfTens = min(numOfTwos, numOfives)
        return numOfTens
    else:
        return numOfTens

if __name__ == '__main__':
    while True:
        userInput = input("enter the number or press q to quit: ")
        if userInput != 'q':
            try:
                num = int(userInput)
            except ValueError:
                print("invalid entry. Please enter an integer or enter 'q' to quit")
                continue
            else:
                try:
                    print(f"The factorial of {num} is {factorial(num)}")
                except Exception:
                    print(Exception)
                print(f"number of trailing zeroes in factorial of {num} is {trailingZeroesInFactorial(num)}")
                continue
        else:
            break



