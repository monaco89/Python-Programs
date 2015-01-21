#Nick Monaco# CMPT 101-01
# Infile Numbers

def main():
    infile= open('Numbers1.txt','r')
    infile2= open('Numbers2.txt','r')
    outfile= open('NumbersAll.txt','w')
    count1=0
    count2=0
    line1=infile.readline()
    line2=infile2.readline()
    while line1!='' and line2!='':
        num1= int(line1)
        num2= int(line2)
        if num1<=num2:
            count1+=1
            outfile.write(line1)
            print(num1)
            line1= infile.readline()
        else:
            count2+=1
            outfile.write(line2)
            print(num2)
            line2= infile2.readline()
    while line1!='':
        count1+=1
        outfile.write(line1)
        num1= int(line1)
        print(num1)
        line1.infile.readline()
    while line2!='':
        count2+=1
        outfile.write(line2)
        num2=int(line2)
        print(num2)
        line2=infile2.readline()
    infile.close()
    infile2.close()
    outfile.close()
    print("There are",count1,"numbers in file 1")
    print("There are",count2,"numbers in file 2")        

main()
