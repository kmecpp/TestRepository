# Author: kmecpp
# - Some Amazhing Python Code -
# (Jk this is just a test)

def main():
    try:
        x = eval(input("Enter a number: "))
        print(str(x) + " squared equals, " + str(x*x))
    except (NameError, SyntaxError):
        inputError()
        
def inputError():
    print("I said enter number yah potato!!")
    input()
    main()

main()
