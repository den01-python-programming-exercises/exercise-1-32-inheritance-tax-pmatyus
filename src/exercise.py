def main():
    #write your code below this line
    inheritance = int(input("Inheritance:"))
    years = int(input("Years since death:"))
    taxable = 0
    tax = 0
    if (inheritance > 325000):
      taxable = inheritance - 325000
    if (years < 3):
      tax = (taxable *0.4)
    elif (years < 4):
      tax = (taxable *0.32)
    elif (years < 5):
      tax = (taxable *0.24)
    elif (years < 6):
      tax = (taxable *0.16)
    elif (years < 7):
      tax = (taxable *0.08)
    elif (years >= 7):
      tax = (taxable * 0)
    print("Tax: " + str(tax))

if __name__ == '__main__':
   main()

