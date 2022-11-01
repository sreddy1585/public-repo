
def addition(a, b):
    c = a + b
    return (c)


def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print("The sum of these two numbers is ", end="")
    print(addition(a, b))

if __name__ == '__main__':
    main()