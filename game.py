import random
class gameObj:
	def __init__(self,name,beats):
		self.name = name
		self.beats = beats
		objList.append(self)
		
objList = []
rock = gameObj('rock',['scissors','cockroach'])
paper = gameObj('paper',['rock','cockroach'])
sciss = gameObj('scissors',['paper','cockroach'])
nuke = gameObj('nuclear bomb',['rock','paper','scissors'])
roach = gameObj('cockroach','nuclear bomb')

playerInput = input()
playerInput = playerInput.lower()
for i in objList:
	if playerInput == i.name:
		playerHand = i
		break
cpuHand = objList[random.randint(0,len(objList)-1)]

if cpuHand.name in playerHand.beats:
	print('You win!')
elif playerHand.name in cpuHand.beats:
	print('You lose!')
else:
	print('No clear winner')
print('You chose '+playerHand.name)
print('Computer chose '+cpuHand.name)
