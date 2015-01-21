def main():
    table=[[0,0,0],[0,0,0]]
    print(table)
    num=0
    for row in range(2):
        for col in range(3):
            table[row][col]=num
            num+=2
    for row in range(2):
        for col in range(3):
            print(table[row][col],end="\t")
        print()

main()
