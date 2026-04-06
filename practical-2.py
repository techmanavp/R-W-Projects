
print("Welcome to the pattern Generator and Number Analyzer !")
print()

print("Select an option:\n1. Generate Pattern\n2. Analyze a Range of Numbers\n3. Exit")

choice = int(input("Please Enter your Choice:"))

match choice:
    case 1:
        print()
        print("You have selected option 1\n1. Half Pyramid  \n2. Inverted Half Pyramid")
        p = int(input("Enter Pattern Choice number:"))
        print()
        
        match p:
            case 1:
                 rows = int(input("Enter number of Rows for the pattern: "))
                 for i in range(1,rows+1):
                     for j in range(i):
                         print("*", end=" ")
                     print()
            
            case 2:
                rows = int(input("Enter number of Rows for the pattern: "))
                for i in range(1,rows + 1):
                    for j in range(i,rows+1):
                        print("*", end=" ")
                    print()
            case _:
                print("Enter Valid Option")
        
    
    case 2:
        print()
        print("You have selected option 2")
        
        a = int(input("Enter the start of the range:"))
        b = int(input("Enter the end of the range:"))
        
        total = 0
        for i in range(a,b+1):
            if i % 2 == 0:
                print("Number",i,"is Even")
            else:
                print("Number",i,"is Odd")
            total = total + i
        print("The Total of",total)
        
        
        
    case 3:
        print("Exiting the program. Goodbye !")
        
    case _:
        print("Enter Valid Option")