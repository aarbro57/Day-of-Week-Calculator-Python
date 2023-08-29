
def printHeading():
    print('*******************************')
    print('      Birthday Calculator      ')
    print('*******************************')

def printCloser():
    print()
    print('****************************************************')
    print('      Thanks for using the Birthday Calculator      ')
    print('****************************************************')

def printMenu():
    print()
    print('Menu Options')
    print('------------')
    print('1) Determine day of birth')
    print('2) Print the next 10 leap years')
    print('3) Finished')
    print()
    print('Choice --> ')

def getMenuChoice():
    printMenu()
    choice = input()
    choice = int(choice)

    while choice != 1 and choice != 2 and choice != 3:
        print()
        print('Invalid menu choice')
        printMenu()
        choice = input()
        choice = int(choice)

    if choice == 1:
        return 1
    elif choice == 2:
        return 2
    else:
        return 3

def isGregorianDate(month, day, year): 
    if year > 1752:
        return True
    elif year == 1752:
        if month > 9:
            return True
        elif month == 9:
            if day == 13:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
        
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def isValidDate(month, day, year):
    if isGregorianDate(month, day, year):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day >= 1 and day <= 31:
                return True
            else:
                return False
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day >= 1 and day <= 30:
                return True
            else:
                return False
        elif month == 2:
            if isLeapYear(year):
                if day >=1 and day <= 29:
                    return True
                else:
                    return False
            else:
                if day >= 1 and day <= 28:
                    return True
                else:
                    return False
        else:
            return False
    else: return False

def determineDay(month, day, year):
    zMonth = 0
    zYear = 0
    C = 0
    Y = 0
    f = 0

    if month == 1 or month == 2:
        zMonth = month + 12
        zYear = year - 1
    else:
        zMonth = month
        zYear = year
    
    C = int(zYear / 100)
    Y = zYear - (C * 100)

    f = int((day + int((13 * (zMonth + 1))) / 5 + Y + int(Y / 4) + int(C / 4) + 5 * C)) % 7
    return f

def printDayOfBirth(day):
    if day == 1:
        print('Sunday')
    elif day == 2:
        print('Monday')
    elif day == 3:
        print('Tuesday')
    elif day == 4:
        print('Wednesday')
    elif day == 5:
        print('Thursday')
    elif day == 6:
        print('Friday')
    else:
        print('Saturday')

def determineDayOfBirth():
    print()
    print('Enter your date of birth')
    print('format: month / day / year    -->')
    DATE = input()
    date = DATE.split()
    month = int(date[0])
    day = int(date[2])
    year = int(date[4])
    print()
    if not isValidDate(month, day, year):
        print('Invalid Date')
    else:
        print('You were born on a:', end= ' ')
        printDayOfBirth(determineDay(month, day, year))
        print()
        print('Have a great birthday!!!')
    print()

def print10LeapYears():
   
    print()
    print('Enter year --> ')
    year = input()
    year = int(year)
    print()
    i = 0
    if year >= 1752:
        while i < 10:
            year += 1
            if isLeapYear(year):
                print('Leap year is', end=' ')
                print(year)
                i += 1

printHeading()
choice = getMenuChoice()

while choice != 3:
    if choice == 1:
        determineDayOfBirth()
        choice = getMenuChoice()
    elif choice == 2:
        print10LeapYears()
        choice = getMenuChoice()
printCloser()
