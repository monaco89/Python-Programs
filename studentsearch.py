def search(students,lookfor):
    location=0
    found=0
    index=0
    n=5
    while index < n and found!=1:
        if lookfor== students[index]:
            location= index+1
            found=1
        else:
            index+=1
    return location

def main():
    lookfor= input("Enter a name:")
    students=['sam','bill','kate','ginny','george']
    location= search(students,lookfor)
    if location>0:
        print(lookfor,"is in the list at position",location)
    else:
        print(lookfor,"is not in the list")

main()
