def getPrice():
    p= eval(input("price of the item: "))
    return p

def discount(p):
    d= p*.2
    return d

def printTitle():
    print("Discount Calculator")

def printSale(sale):
    print(sale)

def main():
    #again='y'
    #while again.lower()=='y':
        printTitle()
        getPrice()
        discount()
        sale= p-d
        printSale()
        #again= input("another?: ")
    
