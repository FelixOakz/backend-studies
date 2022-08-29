# first step to accept name and quantity of the product. This process done repeatedly until all products entered
# once are all accepted, we will accept consumer's supermarket membership, and a discount depending on it
# gold - 20%, silver - 10% and bronze, 5%
# finally, calculate total bill depending on the products and print detailed bill to output screen



#1 Creating simple function which will accept: name and price of the product (dictionary)
def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input("Press A to add product and Q to quit: ")
        if details == "A":
            product = input("Enter Product: ")
            quantity = int(input("Enter quantity:"))
            buyingData.update({product:quantity})
        elif details == "Q":
            enterDetails = False
        else:
            print("Please select a correct option, A to add or Q to quit.")
    return buyingData

#2 Having product details, need to calculate total price. WOnt be final price since still need to check discount
def getPrice(product, quantity):
    priceData = {
        "Biscuit":3,
        "Chicken":5,
        "Egg":1,
        "Fish":3,
        "Coke":2,
        "Bread":2,
        "Apple":3,
        "Onion":3
    }
    subtotal = priceData[product] * quantity
    print(product + ":$" + str(priceData[product]) + "x" + str(quantity) + "=" + str(subtotal))
    return subtotal

#3 after getting subtotal amount, check whether client has membership in supermarket, discount is bill > $25
def getDiscount(billAmount, membership):
    discount = 0
    if billAmount >= 25:
        if membership == "Gold":
            billAmount = billAmount * 0.80
            discount = 20
        elif membership == "Silver":
            billAmount = billAmount * 0.90
            discount = 10
        elif membership == "Bronze":
            billAmount = billAmount * 0.95
            discount = 5
        print(str(discount) + "% off for " + membership + " " + "membership on total amount: $" + str(billAmount))
    else:
        print("Sorry, no discount on amount less than $25")
    return billAmount

#4 making the calls to function, and make bill to the purchased products
def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    billAmount = getDiscount(billAmount, membership)
    print("The discounted amount is $" + str(billAmount))

#Trigger program with apropriate function call so that the whole flow gets into action
buyingData = enterProducts()
membership = input("Enter customer membership: ")
makeBill(buyingData, membership)
