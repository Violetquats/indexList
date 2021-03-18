# indexList
"""
Program goals:
1. Get user input
2. Convert the input to input
3. Add input to list
4. Full values from specific input positions
"""
#create functions that will perform those actions above
myList = []
import random
def mainProgram():
    while True:
        try:
            print("Hello!")
            print("Choose one of the following options. Type numbers ONLY!")
            choice = input("""
1. Add to list,
2. Add a lot of numbers to your list,
3. Return the value at an index position,
4. Print contents of list
5. Random choice,
6. Linear search,
7. Exit the program  """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addManyItems()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                print(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            else:
                break
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

def randomSearch():
    print("Here's a random value from your list!  ")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're gonna search every single item like a moron! WHOOO!")
    searchItem = input("What do ya wanna find?"  )
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))
    

if __name__ == "__main__":
    mainProgram()
