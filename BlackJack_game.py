import random
number=['ACE',2,3,4,5,6,7,8,9,10,'JACK','QUEEN','KING']
card=['HEART','DIAMAND','CLUB','SPADE']
hit,END,bust=1,False,False

#create the game point
playerPoint,dealarPoint,deck=[],[],[]
point1,point2=0,0
function={"1":"ACE","11":"JACK","12":"QUEEN","13":"KING"}

#create new cards for the specified player 
for i in number:
	for j in card:
		deck.append([i,j])
random.shuffle(deck)

#get cards
def playcard(player,cardNum):
	for i in range(cardNum):
		temp_num=deck.pop(0)
		if(temp_num[0]=='ACE'): temp_num[0]=1
		elif temp_num[0]=='JACK' or temp_num[0]=='QUEEN' or temp_num[0]=='KING': 
			temp_num[0]=10
		player+=temp_num

#compute points of the owning cards
def point(cards,pointnum):
	count=cards.count(1)
	#case(1):get ACE lastly case(2):get ACE before and has been counted
	if count==1 and ((pointnum<=10 and cards[len(cards)-2]==1) or 
					(cards[len(cards)-2]!=1 and pointnum+cards[len(cards)-2]<=21)): 
		pointnum=sum(cards[0:len(cards):2])+10
	else:
		pointnum=sum(cards[0:len(cards):2])
	return pointnum

#main game function
def GAME(player,currentPoint,ifbust,cardnum):
	playcard(player,cardnum)
	if player is playerPoint:	
		string="You" 
		string2="draw"
	else:	
		string="Dealer" 
		string2="draws"

	if cardnum==1:
		cards=number[player[len(player)-2]-1]
		print(string,string2,cards,'-',player[len(player)-1],end="\n")
		print()

	currentPoint=point(player,currentPoint) #compute points

	#output the result
	if currentPoint<21:
		print(string,"r current value is ",currentPoint,sep='')
	elif currentPoint==21:
		print(string,"current value is Blackjack! (21)")
	else: 
		print(string,"current value is Bust! (>21)")
	print("with the hand:",end=" ")

	#current cards
	for i in range(0,len(player)-2,2):
		numbers=number[player[i]-1]
		print(numbers,'-',player[i+1],sep='',end=', ')
	print(player[len(player)-2],'-',player[len(player)-1],sep='')
	print()
	return currentPoint

def ask():  #if continue the game
	hit=int(input("Hit or stay?(Hit = 1, Stay = 0): "))
	print()
	return hit

def UNWIN(player):  #output the winner by calling the loser
	if player is playerPoint:
		print("*** Dealer win! ***")
	else:
		print("*** You beat the dealer! ***")

def again():
	char=input("Want to play again?(y/n): ")
	print()
	if char=='y':	
		print("--------------------------")
		return False
	else: return True

while END==False:
	playerPoint,dealarPoint=[],[]
	point1,point2=0,0
	point1=GAME(playerPoint,point1,bust,2) #get cards
	hit=ask()
	
	while hit==1 and point1<21:  #if out of 21 points then out of the loop
		point1=GAME(playerPoint,point1,bust,1)
		if point1<21:
			hit=ask()
			print()

	if point1>21:  #player loses the game 
		UNWIN(playerPoint)
		END=again() 
		continue

	hit=1  #if player < 21point, then the game continues
	point2=GAME(dealarPoint,point2,bust,2)
	while hit==1 and point2<17:
		point2=GAME(dealarPoint,point2,bust,1)
		if point2>17:
			hit=0
	if point2>21:
		UNWIN(dealarPoint)
		END=again()
		continue

	#determine which is the winner
	if point1>point2:
		UNWIN(dealarPoint)
	elif point2>point1:
		UNWIN(playerPoint)
	else: print("*** You tied the dealer, nobody wins. ***")
	END=again()