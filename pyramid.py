def print_pyramid(height):
    # Initialize the current row
    row = 0
    
    # Outer loop for each row
    while row < height:
        # Initialize spaces for the current row
        spaces = 0
        
        # Print leading spaces
        while spaces < height - row - 1:
            print(" ", end="")
            spaces += 1
        
        # Initialize asterisks for the current row
        stars = 0
        
        # Print asterisks for the current row
        while stars < (2 * row + 1):
            print("*", end="")
            stars += 1
        
        # Move to the next line after printing a row
        print()
        
        # Move to the next row
        row += 1

# Get height input from user
try:
    height = int(input("Enter the height of the pyramid: "))
    if height > 0:
        print_pyramid(height)
    else:
        print("Please enter a positive integer.")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    