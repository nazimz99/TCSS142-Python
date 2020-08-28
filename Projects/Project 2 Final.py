#Nazim Zerrouki
#TCSS 142 David Schuessler Project 2
#12/01/17
def main(): #defines the "main function" in which every piece of code is outputted through this function.
    response = 'y'
    while response == 'Y' or response == 'y': #Keeps the loop running as long as the responder answers y or Y.
        napier_1 = findNapier() #Calls the function used to find the decimal value of the first value the user inputs in napier notation.
        value_1 = calcNapier1(napier_1) #Calls the function that uses the first value in napier notation as an argument.
        print("The first number is", value_1) #Prints out the first napier value in decimal form.
        napier_2 = findNapier() #Calls the function used to find the decimal value of the second value the user inputs in napier notation.
        value_2 = calcNapier2(napier_2) #Set a variable equal to a function used to find the decimal value of the second value the user inputs in napier notation.
        print("The second number is", value_2) #Prints out the second napier value in decimal form.
        operator = findArithmetic() #Set a variable equal to a function which asks the user what arithmetic operation the user wants to use and makes calculations based on the user's choice.
        value_sum = calcArithmetic(value_1, value_2, operator) #The main function calls the total decimal value found in this function which uses the decimal values and the arithmetic operation the user inputs. 
        binary = calcBinary(value_sum)
        if value_sum < 0: #Prints out the total in decimal form and the sum in napier notation as a negative if the decimal total is negative as well.
            print("The result is", value_sum, "or", end = ' ')
            print("-", end = '')
            alterBinary(binary)
        elif value_sum > 0: #Prints out the total in decimal form and the sum in napier form as a positive value if the total in decimal form is positive as well.
            print("The result is", value_sum, "or", end = ' ')
            alterBinary(binary)
        else: #Prints out the total in decimal form only if the sum is 0. A napier value does not exist if said value is 0.
            print("The result is", value_sum, end = ' ')
        print()
        response = input("Do you want to repeat the program? Enter y for yes, n for no: ") #Asks the user if they want to continue. Continues the loop/program if the answer is y or Y and stops the progam if the answer is any other value.

def findNapier(): #Defines the function used to prompt the user for a napier value with multiple statements.
    napier = str(input("Enter Napier's number: ")) #Prompts the user of a value in napier notation.
    napier = napier.lower()
    while not napier.isalpha(): #Sets a condition that traps the user into a loop if the value doesn't consist only of letters.
        print("Something is wrong. Please try again.")
        napier = str(input("Enter Napier's number: "))
    return napier #returns the napier value the user input to be called by the main function. This allows napier to be used by my other functions that is used to convert both napier values into decimal form.

def calcNapier1(napier): #Defines the function used to calculate the decimal of the first napier value with multiple statements.
    napier1 = 0 #Initializes the variable used to calculate decimal #1.
    for ch in napier: #Checks each character in the first napier value.
            napier1 += 2**(ord(ch) - ord('a')) #Adds the 2 ** ordinal value of each character subtracted by the ordinal value of a to create a series of numbers to calculate the decimal value.  
    return napier1 #Returns the first decimal to main, so it can be used by other parts of the code.

def calcNapier2(napier):
    napier2 = 0 #Initializes the second decimal value.
    for ch in napier: #Checks each character in the second napier value.
        napier2 += 2**(ord(ch) - ord('a')) #Increments the variable in the same way that was done to calculat the first decimal. 
    return napier2 #Returns the second decimal to main, so it can be used by other parts of the program.

def findArithmetic(): #Defines the function used to find the arithmetic operation with multiple statements.
    arithmetic = input("Enter the desired artithmetic operation: ") #Prompts the user to enter the operation used to calculate the sum.
    while arithmetic not in "+-*/": #A while loop that ensures that the program will not continue until the user inputs an artihmetic operation.
        print("Something is wrong. Please try again.")
        arithmetic = input("Enter the desired arithmetic operation: ")
    return arithmetic #returns the arithmetic operation to main, so it can be used by other parts of the program.

def calcArithmetic(napier1, napier2, arithmetic): #Defines a function used to calculate the total by using both decimal values and the arithmetic operation that were returned to main.
    if arithmetic == '+':
        total = napier1 + napier2 #Calculates the sum of two napier values the user inputs if the aritmetic operation implies addition.
    elif arithmetic == '-':
        total = napier1 - napier2 #Calculates the difference of two napier values the user inputs if the arithmetic operation implies subtraction.
    elif arithmetic == '*':
        total = napier1 * napier2 #Calculates the product of two napier values the user inputs if the arithmetic operation implies multiplication.
    elif arithmetic == '/':
        import math
        total = math.ceil(napier1 / napier2) #Performs float division on two napier values the user inputs and rounds it up if the arithmetic operation implies division.
    return total #Returns the total of these two decimal values to the main, so it can be used by other parts of the program.

def calcBinary(total): #A function that uses the total of both decimals to convert the decimal in binary form.
    total_list = [ ] #Creates a list to contain each digit or remainder of the total if it were divided by two.
    while total != 0: #Creates a while loop to keep dividing the total by two until the quotient is zero.
        if total < 0:
            total = total * -1 #An infinite loop of dividing yhe total by two is created unless the total is positive, so this loop is to ensure that the quotient reaches zero.
        binary = total % 2
        total = total // 2
        total_list.append(binary) #Appends each remainder to the list, so it creates a list of binary code in reverse for every decimal value.
    return total_list #Returns the list containing each remainder to main, so it can be used by the other parts of the program.

def alterBinary(total_list): #A function that uses the list of binary code to print out the decimal as the sum of letters (napier notation) with no repeating letters.
    for i in range(len(total_list)):
        if total_list[i] != 0:
            print(chr(i + ord('a')), end = '') #Prints out the character value of the digit in respect to its position as long as the remainder is not zero. A zero value implies absence of value and should not be considered.

main() #Executes the entire main function that contains the program.
