'''Problem statement:- take input from the user and convert it to the users desirable currency'''
# First go to this website - 'https://www.x-rates.com/table/?from=INR&amount=1' and copy the data. After copying the data paste it inside a text file

with open('CurrencyData.txt') as f:
    currencyData = f.readlines()

currDict = {}
for line in currencyData:
    parsed = line.split('\t')
    currDict[parsed[0]] = parsed[1]

value = float(input("Indian rupees: \n"))
print("Convert to: ")
[print(item) for item in currDict.keys()]
currencyName = input("choose from above options: ")

convertedValue = float(currDict.get(currencyName)) * value
print(f"{value} INR = {convertedValue} {currencyName}")
