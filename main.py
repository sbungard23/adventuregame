currentPos = "a"
print(currentPos)


def functionA() :
  global currentPos
  while currentPos == 'a':
    answer = input("which way would you like to move?       ")
    if answer == "forward":
      print("A wall blocks you. Try another direction.")

    if answer == "right":
      print("You walk through a door to your right.")
      currentPos = 'b'
      print(currentPos)
      functionB()
  
    if answer == "backward":
      print("you walk through a door behind you")
      currentPos = 'd'
      print(currentPos)
      functionD()

    if answer == "left":
      print("A wall blocks you. Try another direction.")

def functionB() :
  global currentPos
  while currentPos == 'b':
    answer = input("which way would you like to move?       ")
    if answer == "forward":
      print("A wall blocks you. Try another direction.")

    if answer == "right":
      print("You walk through a door to your right.")
      currentPos = 'c'
      print(currentPos)
      functionC()
  
    if answer == "backward":
      print("you walk through a door behind you")
      currentPos = 'e'
      print(currentPos)
      functionE()

    if answer == "left":
      print("you walk through a door to your left")
      currentPos = 'a'
      print(currentPos)
      functionA()

def functionC() :
  global currentPos
  while currentPos == 'c':
    answer = input("which way would you like to move?       ")
    if answer == "forward":
      print("A wall blocks you. Try another direction.")

    if answer == "right":
      print("A wall blocks you. Try another direction.")

    if answer == "backward":
      print("you walk through a door behind you")
      currentPos = 'f'
      print(currentPos)
      functionF()
      
    if answer == "left":
      print("You walk through a door to your left.")
      currentPos = 'b'
      print(currentPos)
      functionB()

def functionD() :
  global currentPos
  while currentPos == 'd':
    answer = input("which way would you like to move?       ")
    if answer == "forward":
      print("you walk through a door in front of you")
      currentPos = 'a'
      print(currentPos)
      functionA()

    if answer == "right":
      print("you walk through a door to your right")
      currentPos = 'e'
      print(currentPos)
      functionE()

    if answer == "backward":
      print("you walk through a door behind you")
      currentPos = 'g'
      print(currentPos)
      functionG()
      
    if answer == "left":
      print("A wall blocks you. Try another direction.")

def functionE() :
  global currentPos
  while currentPos == 'e':
    answer = input("which way would you like to move?       ")
    if answer == "forward":
      print("you walk through a door in front of you")
      currentPos = 'b'
      print(currentPos)
      functionB()

    if answer == "right":
      print("you walk through a door to your right")
      currentPos = 'f'
      print(currentPos)
      functionF()

    if answer == "backward":
      print("you walk through a door behind you")
      currentPos = 'h'
      print(currentPos)
      functionH()
      
    if answer == "left":
      print("you walk through a door to your left")
      currentPos = 'd'
      print(currentPos)
      functionD()

def functionF() :
  global currentPos
  while currentPos == 'f':
    answer = input("which way would you like to move?       ")
    if answer == "forward":
      print("you walk through a door in front of you")
      currentPos = 'c'
      print(currentPos)
      functionC()

    if answer == "right":
      print("A wall blocks you. Try another direction.")

    if answer == "backward":
      print("you walk through a door behind you")
      currentPos = 'i'
      print(currentPos)
      functionI()
      
    if answer == "left":
      print("you walk through a door to your left")
      currentPos = 'e'
      print(currentPos)
      functionE()

def functionG() :
  global currentPos
  while currentPos == 'g':
    answer = input("which way would you like to move?       ")
    if answer == "forward":
      print("you walk through a door in front of you")
      currentPos = 'd'
      print(currentPos)
      functionD()

    if answer == "right":
      print("you walk through a door to your right")
      currentPos = 'h'
      print(currentPos)
      functionH()

    if answer == "backward":
      print("A wall blocks you. Try another direction.")
      
    if answer == "left":
      print("A wall blocks you. Try another direction.")

def functionH() :
  global currentPos
  while currentPos == 'h':
    answer = input("which way would you like to move?       ")
    if answer == "forward":
      print("you walk through a door in front of you")
      currentPos = 'e'
      print(currentPos)
      functionE()

    if answer == "right":
      print("you walk through a door to your right")
      currentPos = 'i'
      print(currentPos)
      functionI()

    if answer == "backward":
      print("A wall blocks you. Try another direction.")
      
    if answer == "left":
      print("you walk through a door to your left")
      currentPos = 'g'
      print(currentPos)
      functionG()

def functionI() :
  global currentPos
  while currentPos == 'i':
    answer = input("which way would you like to move?       ")
    if answer == "forward":
      print("you walk through a door in front of you")
      currentPos = 'f'
      print(currentPos)
      functionF()

    if answer == "right":
      print("A wall blocks you. Try another direction.")

    if answer == "backward":
      print("A wall blocks you. Try another direction.")
      
    if answer == "left":
      print("you walk through a door to your left")
      currentPos = 'h'
      print(currentPos)
      functionH()
      
      
      
functionA()