# Nick Monaco
# CMPT 101-01
# 10/9/12
# BMI
import math
def main():
    weight= eval(input("enter weight: "))
    height= eval(input("enter height: "))
    BMI= (weight*720)/(height**2)
    if BMI<25 and BMI>19:
        print("You are within the healthy range")
    elif BMI<19:
        print("You are below the healthy range")
    elif BMI>25:
        print("You are above the healthy range")
