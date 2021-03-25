# indexList
myList = []
import random
def mainProgram():
    while True:
        try:
            print("Hello!")
            print("Choose one of the following options, but please only type numbers!")
            choice = input("""
1. Add a single item to your list,
2. Add a lot of randomized numbers to your list,

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
    

if __name__ == "__main__":
    mainProgram()
