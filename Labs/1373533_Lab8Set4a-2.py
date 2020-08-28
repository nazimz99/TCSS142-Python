#Nazim Zerrouki
#12/02/17
def main():
    response = 'y'
    while response == 'y' or response == 'Y':
        num = int(input('Enter a number of terms: '))
        total = ex3a(num)
        sequence = 4 ** (num - 1)
        print("The sum of the geometric series from 1 to {} is {}".\
              format(sequence, total))
        total = ex3b(num)
        print("The sum of the arithmetic series from 1/3 to {}/3 is {:.5f}".format(num, total))
        word = input("Enter a word: ")
        while not word.isalpha():
            print("Something is wrong. Please try again.")
            word = input("Enter a word: ")
        isReverse = ex3c(word)
        negation = 'not '
        if isReverse:
            negation = ''
        print("The word {} is {}in reverse alphabetical order".format(word, negation))
        response = input("Would you like to repeat this program? Enter y for yes, n for no: ")
        
def ex3a(num):
    sum1 = 0
    for n in range(num):
        sum1 += 4 ** n
    return sum1

def ex3b(num):
    sum2 = 0
    for n in range(1, num + 1):
        sum2 += ((1 / 3) * n)
    return sum2

def ex3c(word):
    alpha = [ ]
    in_order = [ ]
    word = word.lower()
    for ch in word:
        alpha.append(ord(ch))
        in_order.append(ord(ch))
    in_order.sort()
    in_reverse = in_order[::-1]
    if alpha == in_reverse:
        return True
    else:
        return False

                    
main()
