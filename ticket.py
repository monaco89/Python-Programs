#Nick Monaco
#Cmpt 101-01
#Speeding Ticket

def ticket(limit,speed):
    tckt=(speed-limit)*5+50
    if speed>90:
        tckt=tckt+200
    return tckt

def main():
    speed=eval(input("what was the speed: "))
    limit= eval(input("what was the speed limit: "))
    tckt= ticket(limit,speed)
    if speed>limit:
        print("The car was speeding, the ticket is:",tckt)
    else:
        print("The car was under the limit")
