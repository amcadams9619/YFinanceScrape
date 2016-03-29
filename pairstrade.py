import stockLib as s
import ValLib as v
           
print("--- Pairs Trading Analysis Tool ---") 
print("\nPurpose:")
print("This program will analyze the relationship between the\nopening price of 'stock 1'",
      "and the closing price of 'stock 2'")
print("_____________________________________________________________\n")

symbol1 = input("Enter ticker symbol for 'stock 1': ")
symbol2 = input("Enter ticker symbol for 'stock 2': ")
print("Please wait a few seconds...")

stock1 = s.Stock(symbol1,"o")
stock2 = s.Stock(symbol2,"c")

run_again = "y"
while (run_again != "n") :
    
    print("\n--- Commands ---\n")
    print("(1) Analyze, (2) View Data, (3) Visualize, (4) Change Stocks, (5) Exit")
    command = input("\nSelect a command number: ")
    command = int(command)

    if (command == 1) :
        analyze = s.reg_summary(stock1,stock2)
        print(analyze)

    elif (command == 2) :
        v.view_data(symbol1,symbol2)
        #print("\nA:",symbol2.upper()," B:",symbol1.upper())
        #print(view_data)

    elif (command == 3) :
        print("\nPlaceholder for matplotlib script.")

    elif (command == 4) :
        symbol1 = input("Enter ticker symbol for 'stock 1': ")
        symbol2 = input("Enter ticker symbol for 'stock 2': ")
        print("Please wait a few seconds...")

        stock1 = s.Stock(symbol1,"o")
        stock2 = s.Stock(symbol2,"c")

    elif (command == 5) :
        print("\nThank you for stopping by. Goodbye.")
        run_again = "n"

    else :
        print("\nNot a valid command. Try again.\n")
