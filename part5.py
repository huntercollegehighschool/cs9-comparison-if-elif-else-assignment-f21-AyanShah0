'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below
day31 = ['January', 'january', 'March', 'march', 'May', 'may', 'July', 'july', 'August', 'august', 'October', 'october', 'December', 'december']
day30 = ['April', 'april', 'June', 'june', 'September', 'september', 'November', 'november']
ViableMonth = 0

Month = str(input('Enter a month: '))

while ViableMonth == 0:
    if Month in day30:
        print('That month has 30 days')
        ViableMonth = 1
    elif Month in day31:
        print('That month has 31 days')
        ViableMonth = 1
    elif Month == 'February' or Month == 'february':
        print('That month has either 28 or 29 days.')
        ViableMonth = 1
    else:
        print('That month does not exist. Please try again.')
        Month = str(input('Enter a month: '))