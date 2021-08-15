''' Problem statement:- So we have to create an application which will take input from the user and add it until the user presses his enter key and then display the total price. This is a basic application whih can be used in stores to calculate and generate bill. This application will keep store the numbers user has put and will add them until the user presses "q" on their keyboard. Then the application will print the result as a bill. '''

import datetime
import random
def billGenerator(total, *args):
    date = datetime.datetime.now()
    with open("myBill.txt", 'a+') as bill:
        bill.write(f"\nDate-time: {date}")
        for key, value in args:
            bill.write(f"\n{key} = {value}")
        bill.write(f"\nTotal amount = {total}")


totalPrice = 0
prices = []
orders = []
print("********************** Welcome to Arjun kiraana store!!! *******************************")
while True:
    orderItem = input("please enter the name of item or press q to quit: ")
    checkAlpha = orderItem.isalpha()
    if checkAlpha == False: 
        print("Inavalid item name. Please enter only alphabetic string")
        continue
    elif orderItem == 'q':
        billItems = tuple(zip(orders, prices))
        billGenerator(totalPrice, *billItems)
        print(f"Thank you, your total amount = {totalPrice}. Please visit our store again.")
        break
    else:
        itemPrice = input(f"please enter the price of the {orderItem}: ")
        try:
            price = int(itemPrice)
        except ValueError:
            print("Invalid entry. Please enter an integer as price")
            continue
        else:
            orders.append(orderItem)
            prices.append(price)
            totalPrice += int(price)
            print(f"your current amount is {totalPrice}")
            

