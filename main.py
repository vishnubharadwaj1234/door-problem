from random import randint
from random import seed

winCount = 0
loseCount = 0
closedDoors = 3
TRIALS = 10000

seed()
for i in range(TRIALS):
  prizeDoor = randint(1,3) 
  playerDoor = randint(1,3) 
  while closedDoors > 2:
    hostDoor = randint(1,3) 
    if hostDoor == prizeDoor or hostDoor == playerDoor:
      continue
    closedDoors -= 1

  if hostDoor == 2 and playerDoor == 3:
   playerDoor = 1
  elif hostDoor == 1 and playerDoor == 2:
    playerDoor = 3
  elif hostDoor == 3 and playerDoor == 1:
    playerDoor = 2
  elif hostDoor == 3 and playerDoor == 2:
    playerDoor = 1
  elif hostDoor == 1 and playerDoor == 3:
    playerDoor = 2
  elif hostDoor == 2 and playerDoor == 1:
    playerDoor = 3
    
  if playerDoor == prizeDoor:
    winCount += 1
  else:
    loseCount += 1
  
  closedDoors = 3

winPercentage = int(winCount)/100
losePercentage = int(loseCount)/100
print("Win: " + str(winPercentage) + "%")
print("Lose: " + str(losePercentage) + "%")
print("You have a higher chance of winning if you switch doors.")