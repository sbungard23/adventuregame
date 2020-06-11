firstKey=0
secondKey=0
thirdKey=0
escaped=False

rooms = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
descriptions = ["You are in a small dark room with SHELVES stretching from floor to ceiling. Sitting on the floor in the middle of the room there is a small BOX.", "You step into a greehouse room filled with overgrown vines. Various POTS and PLANTERS hold flowers and cacti.", "You find yourself in what looks like a very dusty living room. There is a tattered COUCH and a TV only playing grey static.", "As you walk in a LIGHT BULB suspended from the ceiling flickers own. It reveals a DOOR almost completely concealed buy dirt and dust. There is a large keyhole.", "You walk into a library. BOOKSHELVES line the walls from floor to ceiling", "You are in a dusty old bedroom. There is a BED and a DESK.", "You find yourself in a kitchen. It has an old fashioned STOVE and many CABINETS.", "This room is covered completely in MIRRORS.", "You can see NOTHING but darkness and there doesn't appear to be any lights you can turn on."]
position = [" + - - - + - - - + - - - + \n |       |       |       | \n |   x   |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |   x   |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |   x   | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |   x   |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |   x   |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |   x   | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |   x   |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |   x   |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |   x   | \n |       |       |       | \n + - - - + - - - + - - - + "]
availableItems = [
['shelves', 'box'], 
['pots', 'planters'], 
['couch', 'tv'], 
['lightbulb', 'door'], 
['bookshelves'], 
['bed', 'desk'], 
['stove', 'cabinets', 'cookies'], 
['mirrors']]

itemDescriptions = {'shelves':"nothing to see here.", 'box':"looks like you need a key to get into this box.", 'pots':'you found a tiny key!', 'planters':'there\'s something to find in this room, keep looking!', 'couch':'nothing to see here.', 'tv':'The old TV flickers on. It asks you for a five digit code.', 'lightbulb':'nothing to see here.', 'door':"You hear the sound of birds chirping outside. This must be the way out! The door is locked and requires a key", 'bookshelves':'nothing to see here.', 'bed': 'nothing to see here.', 'desk':'nothing to see here.', 'stove':'nothing to see here.', 'cabinets':'nothing to see here.',  'cookies':'You found some chocolate chip cookies! yum. You notice a key under them!', 'mirrors':'nothing to see here.'}

def pots() :
  itemDescriptions["box"] = 'That key you found in the pots fits perfectly. The box unlocks and a slip of paper slids out. You might want to write this down for later. \n +-----------+ \n |           | \n | 3 4 5 6 2 | \n |           |\n +-----------+'

def tv() :
  code = input("ENTER THE CODE:")
  if code == "34562" :
    print("CORRECT! \n YOUR NEXT CLUE: There are some freshly baked COOKIES hidden in the kitchen.")
  else:
    print("INCORRECT! \n The code is hidden somewhere in this house, come back when you have found it.")

def door() :
  numberOfKeys = firstKey + secondKey + thirdKey
  if numberOfKeys == 1:
    global escaped
    escaped=True
    print("GAME OVER. YOU ESCAPED.")
  else: 
    print("You have "+ str(numberOfKeys)+ " of out 1 keys. Collect the rest to escape.")

def cookies():
  global firstKey
  firstKey = 1


itemFunctions = { 'pots': pots, 'tv':tv, 'cookies':cookies, 'door':door}
currentPos = "a"
currentIndex = rooms.index(currentPos)

def move() :
  global rooms
  global currentPos
  startPos = currentPos
  currentIndex = rooms.index(currentPos)
  while currentPos == startPos:
    answer = input("Which way would you like to move?          ")
    if answer == "north":
      if currentPos == 'a' or currentPos == 'b' or currentPos == 'c':
        print("A wall blocks you. Try another direction.")
      else:
        currentPos = rooms[currentIndex - 3]
        print("you walk through a door")

    if answer == "east":
      if currentPos == 'c' or  currentPos =='f' or currentPos =='i':
        print("A wall blocks you. Try another direction.")
      else:
        currentPos = rooms[currentIndex +1]
        print("you walk through a door.")
  
    if answer == "south":
      if currentPos == 'g' or  currentPos =='h' or currentPos =='i':
        print("A wall blocks you. Try another direction.")
      else:
        currentPos = rooms[currentIndex +3]
        print("you walk through a door.")

    if answer == "west":
      if currentPos == 'a' or  currentPos =='d' or currentPos =='g':
        print("A wall blocks you. Try another direction.")
      else:
        currentPos = rooms[currentIndex -1]
        print("you walk through a door.")



def findIndex(string):
  global currentIndex
  currentList = availableItems[currentIndex]
  here = False
  for x in currentList:
    if x == string:
      here = True
  return here

print("WELCOME TO THE GAME \n \nThis is a text based adventure game. Your objective is to escape by finding codes, keys, and hidden objects. You can explore different rooms by using the command 'move', then typing the direction (north, east, south, or west). At any time you can look at your position on a map by typing 'position'. You can get information about your surroundings by typing 'look around'. Any words you see that are in all caps are OBJECTS. You can look more closely at any of these objects while you are in the same room by typing 'examine' and the object's name when prompted. Be sure to spell everything correctly or the game may not respond. Always type in lowercase letters. \n")

while escaped == False :
  currentIndex = rooms.index(currentPos)
  userInput = input("What would you like to do?                 ")
  if userInput == 'move':
    move()
  elif userInput == "look around":
    print(descriptions[currentIndex])
  elif userInput == "position":
    print("Your current position: \n" + position[currentIndex])
  elif userInput == "examine":
    itemInput = input("What item would you like to examine?       ")
    if findIndex(itemInput) == True:
      print(itemDescriptions[itemInput])
      if itemInput in itemFunctions:
        itemFunctions[itemInput] ()
    else:
      print("that item is not in this room!")
  else:
    print("that isn't a command")
  
