def createData():
    outfile= open('Sneakers.txt','w')
    print("Enter Data of sneakers")
    again = 'y'
    while again.lower()=='y':
        Mancode= input("Enter manufacturer code:")
        Pcode= eval(input("Enter product code:"))
        price= eval(input("Enter price:"))
        saleprice=0
        sneakstr= Mancode+'\t'+'_'+'\t'+str(Pcode)+'\t'+str(price)+'\t'+str(saleprice)+'\n'
        outfile.write(sneakstr)
        again= input("another(y/n)?:")
    outfile.close()

def company(inventory):
    n= len(inventory)
    for i in range(n):
        ManCode= inventory[i][0]
        if ManCode == 'R':
            Code= 'Reebok'
        elif ManCode == 'A':
            Code= 'Adidas'
        elif ManCode == 'N':
            Code= 'Nike'
        elif ManCode == 'NB':
            Code= 'NewBalance'
        elif ManCode == 'AS':
            Code= 'Asics'
        elif ManCode == 'C':
            Code= 'Converse'
        elif ManCode == 'D':
            Code= 'DC'
        elif ManCode == 'V':
            Code= 'Vans'
        elif ManCode == 'U':
            Code= 'UGGS'
        elif ManCode == 'T':
            Code= 'Timberland'
        else:
            print("Invalid Manufacturer's Code")
        inventory[i][1]= Code

def getData():
    infile= open('Sneakers.txt','r')
    inventory = infile.readlines()
    n= len(inventory)
    for i in range(n):
        inventory[i] = inventory[i].strip()
        inventory[i] = inventory[i].split('\t')
    return inventory

def display(inventory):
    n= len(inventory)
    col= len(inventory[0])
    for i in range(n):
        for j in range(col):
            print(inventory[i][j],end='\t')
        print()

def sale(inventory):
    n= len(inventory)
    for i in range(n):
        Price= float(inventory[i][2])
        Discount=Price*(.10)
        saleprice=Price-Discount
        inventory[i][4]=str(saleprice)

def writeData(inventory):
    outfile= open('SneakersFinal.txt','w')
    title= "ManufacturerCode Company ProductCode  Price   SalePrice"+'\n'
    outfile.write(title)
    n= len(inventory)
    for i in range(n):
        Mancode= inventory[i][0]
        Code= inventory[i][1]
        Pcode= float(inventory[i][2])
        price= float(inventory[i][3])
        saleprice= float(inventory[i][4])
        sneakstr= Mancode+'\t'+'\t'+Code+'\t'+str(Pcode)+'\t'+'\t'+str(price)+'\t'+str(saleprice)+'\n'
        outfile.write(sneakstr)
    outfile.close()
    
def main():
    createData()
    inventory= getData()
    sale(inventory)
    company(inventory)
    print(inventory)
    display(inventory)
    writeData(inventory)
    
    
main()
                  
    
            
                                                                   
