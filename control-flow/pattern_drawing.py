def print_square(size):
    row = 0
    while row < size:
        for x in range(size):
            print("*", end="")
        print()
        row += 1
    
size = int(input("Enter the size of the pattern: "))

match size:
    case _ if size < 0 :print("Please enter a positive integer.")
    case _ if size >= 0 : print_square(size)
    case _ : print("Invalid input. Please enter a positive integer.")
