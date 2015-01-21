def main():
    phrase= input("Give a phrase:")
    acro= '.'.join([word[0].upper() for word in phrase.split()])
    print(acro)

main()
