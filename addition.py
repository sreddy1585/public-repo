
def addition(a, b):
    c = a + b
    return (c)

def subtraction(a, b):
    c = a - b
    return(c)

def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("The difference between these two numbers is ", end="")
    print(subtraction(a, b))

if __name__ == '__main__':
    main()