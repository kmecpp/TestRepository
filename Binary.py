def main():
    x = input("Enter a binary number: ")
    try:
        newX = int(x)
        if(len(list(str(newX).replace("1", "").replace("0", ""))) > 0):
            inputException()
        else:
            binary = str(newX)
            multiplier = 1
            final = 0
            for char in reversed(binary):
                final += int(char) * multiplier
                multiplier = multiplier*2
            print("Decimal equivilant: " + str(final))
            main()
    except Exception:
        inputException()
        input()
        main()
def inputException():
    print("I said enter a binary number yah potato!")

main()
