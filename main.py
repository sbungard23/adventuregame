currentPos = "a"
import time

rooms = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
descriptions = ["You are in a small dark room with BOOKSHELVES stretching from floor to ceiling. Sitting on the floor in the middle of the room there is a small BOX.", "You step into a greehouse room filled with overgrown VINES. Various POTS and PLANTERS hold flowers and cacti.", "You find yourself in what looks like a very dusty living room. There is a tattered COUCH and a TV only playing grey static.", "As you walk in a LIGHT BULB suspended from the ceiling flickers own. It reveals a DOOR almost completely concealed buy dirt and dust. There are three large keyholes.", "CORNFIELDS surround you, seemingly stretching as far as the eye can see. However after walking for only a minute you run into a wall. The whole room is an optical illusion - the walls are painted the same pale blue shade as the sky even with litte white clouds. How weird.", "You are in a dusty old bedroom. There is a BED and a DESK.", "You find yourself in a kitchen. It has an old fashioned STOVE, CABINETS, and a plate of chocolate chip COOKIES sitting out on a table.", "This room is covered completely in MIRRORS. As you walk farther forward you find yourself surrounded by your own reflection in a labryinth of mirrors.", "You can see NOTHING but darkness and there doesn't appear to be any lights you can turn on."]
position = [" + - - - + - - - + - - - + \n |       |       |       | \n |   x   |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |   x   |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |   x   | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |   x   |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |   x   |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |   x   | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |   x   |       |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |   x   |       | \n |       |       |       | \n + - - - + - - - + - - - + ", " + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |       | \n |       |       |       | \n + - - - + - - - + - - - + \n |       |       |       | \n |       |       |   x   | \n |       |       |       | \n + - - - + - - - + - - - + "]

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
        print("you walk through the door in front of you.")

    if answer == "east":
      if currentPos == 'c' or  currentPos =='f' or currentPos =='i':
        print("A wall blocks you. Try another direction.")
      else:
        currentPos = rooms[currentIndex +1]
        print("you walk through the door to your right.")
  
    if answer == "south":
      if currentPos == 'g' or  currentPos =='h' or currentPos =='i':
        print("A wall blocks you. Try another direction.")
      else:
        currentPos = rooms[currentIndex +3]
        print("you walk through the door to your right.")

    if answer == "west":
      if currentPos == 'a' or  currentPos =='d' or currentPos =='g':
        print("A wall blocks you. Try another direction.")
      else:
        currentPos = rooms[currentIndex -1]
        print("you walk through the door to your right.")

print("WELCOME TO THE GAME \n \nThis is a text based adventure game. You can explore different rooms by using the command 'move', then typing the direction (north, east, south, or west). At any time you can look at your position of a map by typing 'position'. You can get information about your surroundings by typing 'look around'. Any words words you see that are in all caps are OBJECTS. You can look more closely at any of these objects while you are in the same rooms as them by typing 'examine' and the objects name when prompted. Be sure to spell everything correctly or the game may not respond. Always type in lowercase letters. \n")
      
while 1==1:
  currentIndex = rooms.index(currentPos)
  userInput = input("What would you like to do?                 ")
  if userInput == 'move':
    move()
  if userInput == "look around":
    print(descriptions[currentIndex])
  if userInput == "position":
    print("Your current position: \n" + position[currentIndex])
  
  