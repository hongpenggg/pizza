# The function is defined as follows:

bill = {}
makeYourOwnPizza = []

def welcome():
    print("Hello, welcome to the pizza ordering system. Start ordering: ")

def dineIn():
    print("Would you like to dine in or eat out? (D/O)")
    dineIn = input("Option: ")
    
    if dineIn.lower() == "d":
        dineInStatus = "Dine-In"
    elif dineIn.lower() == "o":
        dineInStatus = "Eat Out"
    else:
        print("Please enter a valid choice.")

def specialtyChoice():
    print('''
            Specialty Pizzas:
            1. BBQ Chicken (Chef's Recommendation)
            2. Hawaiian Supreme
            3. Seafood Deluxe (Spicy!)
            4. The Four Cheese (Vegan)
            5. Truffle Shuffle (Vegan)
            6. Tropical Dream (Chef's Recommendation)
        ''')
                
    userChoice = input("Option: ")
    if userChoice == "1":
        pizzaName = "BBQ Chicken"
    elif userChoice == "2":
        pizzaName = "Hawaiian Supreme"
    elif userChoice == "3":
        pizzaName = "Seafood Deluxe"
    elif userChoice == "4":
        pizzaName = "The Four Cheese"
    elif userChoice == "5":
        pizzaName = "Truffle Shuffle"
    elif userChoice == "6":
        pizzaName = "Tropical Dream"
    else:
        print("Invalid choice!")

    userChoice2 = input("What size would you like? (s/m/l): ")

    bill[f"{pizzaName}"] = f"{userChoice2}"

def classicChoice():
    print('''
            Classic Pizzas:
            1. Super Supreme (Contains Beef!)
            2. Beyond Supreme (Vegan)
            3. Meat Galore (Contains Beef!)
            4. Veggie Lovers (Vegan)
            5. Hawaiian (Chef's Recommendation)
            6. Beef Pepperoni (Contains Beef!)
            7. Curry Chicken (Spicy! Chef's Recommendation)
            8. Chicken Supreme
            9. Margherita (Vegan)
        ''')
                
    userChoice = input("Option: ")
    if userChoice == "1":
        pizzaName = "Super Supreme"
    elif userChoice == "2":
        pizzaName = "Hawaiian Supreme"
    elif userChoice == "3":
        pizzaName = "Seafood Deluxe"
    elif userChoice == "4":
        pizzaName = "The Four Cheese"
    elif userChoice == "5":
        pizzaName = "Truffle Shuffle"
    elif userChoice == "6":
        pizzaName = "Tropical Dream"
    elif userChoice == "7":
        pizzaName = "Curry Chicken"
    elif userChoice == "8":
        pizzaName = "Chicken Supreme"
    elif userChoice == "9":
        pizzaName = "Margherita"
    else:
        print("Invalid choice!")

    userChoice2 = input("What size would you like? (s/m/l): ")

    if userChoice == "1":
        bill[f"{pizzaName}"] = f"{userChoice2}"

def newChoice():
    print('''
            New Pizzas:
            1. Mario's Valentines' (Spicy!)
            2. The Impossible Pizza (Vegan)
        ''')
                
    userChoice = input("Option: ")
    if userChoice == "1":
        pizzaName = "Mario's Valentines'"
    elif userChoice == "2":
        pizzaName = "The Impossible Pizza"
    else:
        print("Invalid choice!")

    userChoice2 = input("What size would you like? (s/m/l): ")

    if userChoice == "1":
        bill[f"{pizzaName}"] = f"{userChoice2}"

def promoChoice():
    print('''
            Promotions for Pizzas:
            1. 2-For-1 Hawaiian(Large)
            2. 2-For-1 Pepperoni(Large)
        ''')
                
    userChoice = input("Option: ")
    if userChoice == "1":
        pizzaName = "2-For-1 Hawaiian Large"
    elif userChoice == "2":
        pizzaName = "2-For-1 Pepperoni Large"
    else:
        print("Invalid choice!")

    if userChoice == "1":
        bill[f"{pizzaName}"] = "l"

def makeYourOwn():
    print('''
            Make-Your-Own Pizzas:

            You can add any of the following to your pizza:
            1. Beef Slices
            2. Chicken Pieces
            3. Tomatoes
            4. Pepperoni
            5. Bacon
            6. Truffles
            7. Assorted Cheese (Contains 5 types of cheese!)
            8. BBQ Sauce
            9. Tomato Sauce

            Note that you can only make LARGE pizzas.
        ''')
    choose = True

    while choose != False:           
        userChoice = input("Option: ")
        if userChoice == "1":
            pizzaName = "Beef Slices"
        elif userChoice == "2":
            pizzaName = "Chicken Pieces"
        elif userChoice == "3":
            pizzaName = "Tomatoes"
        elif userChoice == "4":
            pizzaName = "Pepperoni"
        elif userChoice == "5":
            pizzaName = "Bacon"
        elif userChoice == "6":
            pizzaName = "Truffles"
        elif userChoice == "7":
            pizzaName = "Assorted Cheese"
        elif userChoice == "8":
            pizzaName = "BBQ Sauce"
        elif userChoice == "9":
            pizzaName = "Tomato Sauce"
        else:
            print("Invalid choice!")
        
        makeYourOwnPizza.append(pizzaName)

    if userChoice == "1":
        bill[f"{pizzaName}"] = "l"

def menu():
    welcome()
    dineIn()

    validation = True
    while validation != False:
        print("\nWhat would you like to order?\n1. Pizzas\n2. Pasta\n3. Appetisers\n4. Soups & Salads\n5. Entrees\n6. Baked Items\n7. Beverages\n8. Dessert")
        print("Enter your choice by the number. (E.g. '1' for option 1.)")
        userOrderCode = input("Option: ")

        try:
            userOrderCode = int(userOrderCode)
        except:
            print("Invalid input. Please try again.")
            print("Would you like to continue? (y/n): ")
            userContinue = input("Option: ")
            if userContinue == "y":
                validation = True
            else:
                validation = False
        
        if userOrderCode == 1:
            print('''
            Pizzas:
            1. Specialties
            2. Classic Flavours
            3. New
            4. Promotion
            5. Make Your Own
            ''')
            
            userChoice = input("Option: ")
            if userChoice == "1":
                specialtyChoice()
            elif userChoice == "2":
                classicChoice()
            elif userChoice == "3":
                newChoice()
            elif userChoice == "4":
                promoChoice()
            elif userChoice == "5":
                makeYourOwn()
            else:
                print("Invalid choice, try again.")
                print("Would you like to continue? (y/n): ")
                userContinue = input("Option: ")
                if userContinue == "y":
                    validation = True
                else:
                    validation = False
        
        
        elif userOrderCode == 2:
            print()
        
        
        elif userOrderCode == 3:
            print()
       
       
        elif userOrderCode == 4:
            print()
        
        
        elif userOrderCode == 5:
            print()
        
        
        elif userOrderCode == 6:
            print()
        
        
        elif userOrderCode == 7:
            print()
        
        
        elif userOrderCode == 8:
            print()
        
        
        else:
            print("Invalid choice. Please try again.")
            print("Would you like to continue? (y/n): ")
            userContinue = input("Option: ")
            if userContinue == "y":
                validation = True
            else:
                validation = False
        


menu()