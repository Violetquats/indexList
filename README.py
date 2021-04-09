myList = []
uniqueList = []
import random
def mainProgram():
    print("Choose one of the following options ")
    while True:
        try:       
            choice = input("""1. Add a single item to your list,
2. Add a lot of randomized numbers to your list,
3. Return the value at an index position,
4. Sort list,
5. Random choice,
6. Linear search,
7. Binary search,
8. Iterative search,
9. Print your lists,
10. Exit the program  """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addManyItems()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                sortList(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            elif choice == "7":
                binSearch = input("What are you looking for? ")
                recursiveBinarySearch(uniqueList, 0, len(uniqueList)-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What are you looking for? ")
                result = iterativeBinarySearch(uniqueList, int(binSearch))
                if result != -1:
                    print("Your number is at position {}".format(result))
                else:
                    print("Uh oh. Your nuber isn't here :(")
            elif choice == "9":
                printLists()
            elif choice == "10":
                break
            else:
                print("""
Please write an integer between 1 and 10. :D
                      """)
        except:
            print("Uh oh! It looks like an error may have occured!")
        
def addToList():
    newItem = input("Please type an integer.  ")
    myList.append(int(newItem))
    print(myList)

def addManyItems():
    print("Let's add a bunch of numbers!")
    numToAdd = input("How many integers would you like to add?  ")
    numRange = input("How high would you like your numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is now complete")
    
def indexValues():
    indexPos = input("Which item position would you like to see?"  )
    print(myList[int(indexPos)])

def sortList(myList):
    for x in myList:
        if x not in uniqueList:
            uniqueList.append(x)
    uniqueList.sort()
    showMe = input("Would you like to see your unique values? Yes or No  ")
    if showMe.lower() == "yes":
        print(uniqueList)

def randomSearch():
    print("Here's a random value from your list!  ")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("This is a moronic way to search things, but it's fun! WHOOO!")
    searchItem = input("What do ya wanna find?"  )
    indexes = []
    indexCount = 0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            indexes.append(x)
            indexCount = indexCount + 1
    print("Your item is at the index positions:")
    print(indexes)
    print("Your item appeared {} times in your list.".format(indexCount))

def recursiveBinarySearch(uniqueList, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if uniqueList[mid] == x:
            print("Found it! Your number is at position {}".format(mid))
        elif uniqueList[mid] > x:
            return recursiveBinarySearch(uniqueList, low, mid - 1, x)
        else:
            return recursiveBinarySearch(uniqueList, mid + 1, high, x)

    else:
        print("Your number isn't here!")

def printLists():
    if len(uniqueList) == 0:
        print(myList)
    else:
        whichOne = input("Which list--unique or all?  ")
        if whichOne.lower == "unique":
            print(uniqueList)
        else:
            print(myList)

def iterativeBinarySearch(uniqueList, x):
    low = 0
    high = len(uniqueList) - 1
    mid = 0

    while low <= high:
        mid = (high + low) //2

        if uniqueList[mid] < x:
            low = mid +1

        elif uniqueList[mid] > x:
            high = mid -1
        else:
            return mid
    return -1

if __name__ == "__main__":
    mainProgram()
