#Nazim Zerrouki
#12/02/17
def main():
    response = 'y'
    while response == 'y' or response == 'Y':
        import math
        inflate = float(input("Enter a value to calculate the inflation rate: "))
        inflate = math.ceil(inflate)
        for times in range(2, inflate + 1):
            years = CPI_Value(times)
        if times == inflate:
            print("Consumer prices will be {:d} times "\
            "2014 prices in {:d} years ({:d})".\
            format(times, years, 2014 + years))
            response = input("Would you like to repeat this program? Enter y for yes, n for no: ")

def CPI_Value(times):
    value = 238.25
    val = 238.25
    years = 0
    while value < val * times:
        value += value * 0.025
        years += 1
    return years

main()
 
