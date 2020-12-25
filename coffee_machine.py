# Write your code here
water = 400
milk = 540
coffeeB = 120
cups = 9
money = 550

choice = input("Write action (buy, fill, take, remaining, exit):")



def remaining():
    global water
    global coffeeB
    global money
    global milk
    global cups
    print('The coffee machine has:')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(coffeeB) + ' of coffee beans')
    print(str(cups) + ' of disposable cups')
    print('$' +str(money) + ' of money')



def buy():
    global water
    global coffeeB
    global money
    global milk
    global cups
    choiceB = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino, back - to main menu:")
    if choiceB == '1':
        if water < 250:
            print('Sorry not enough water!')
        else:
            water = water - 250
            coffeeB = coffeeB - 16
            money = money + 4
            cups = cups - 1
            print('I have enough resources, making you a coffee!')
    elif choiceB == '2':
        if water < 350:
            print('Sorry not enough water!')
        else:
            water = water - 350
            coffeeB = coffeeB - 20
            milk = milk - 75
            money = money + 7
            cups = cups - 1
            print('I have enough resources, making you a coffee!')
    elif choiceB == '3':
        if water < 200:
            print('Sorry not enough water!')
        else:
            water = water - 200
            milk = milk - 100
            coffeeB = coffeeB - 12
            money = money + 6
            cups = cups - 1
            print('I have enough resources, making you a coffee')
    elif choiceB == 'back':
        return




def fil():
    global water
    global coffeeB
    global money
    global milk
    global cups
    newWater = int(input('Write how many ml of water do you want to add:'))
    water = water + newWater
    newMilk = int(input('Write how many ml of milk do you want to add:'))
    milk = milk + newMilk
    newbeans = int(input('Write how many grams of coffee beans do you want to add:'))
    coffeeB = coffeeB + newbeans
    newCups = int(input('Write how many disposable cups of coffee do you want to add:'))
    cups = cups + newCups









def take():
    global money
    print('I gave you $' + str(money))
    money = 0


while choice != 'exit':
    if (choice == 'buy'):
        buy()
    elif (choice == 'fill'):
        fil()
    elif (choice == 'take'):
        take()
    elif (choice == 'remaining'):
        remaining()
    choice = input("Write action (buy, fill, take, remaining, exit):")


