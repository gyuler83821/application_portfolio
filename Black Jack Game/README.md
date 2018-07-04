# Black Jack Game 二十一點

In this program, it developes a Blackjack game, which allows a user to play against a computer dealer.  

## Game Rules 遊戲規則
The game follows these following rlues:  
* **receive 2 cards separately**: Both player and dealer receive two cards from a shuffled deck of 52 cards 
<font color=#f03c15 face="微軟雅黑">(一副洗好的牌)</font>.  
>   <font color=#f03c15 face="微軟雅黑">先發給玩家跟電腦各兩張牌</font>

* **hit cards:** After receiving first two cards, the player is asked whether he wants another card and then call `hitting`(再抽)), 
or if he is happy with the cards then call `staying`(停止). 
The goal is to make the sum of the player’s card values as close to 21 as possible, without going over. 
If the player makes 21 exactly, he has Blackjack, which cannot be beat.
If the player goes over 21, he `busts`(爆掉) and lose the game. 
The player is allowed to stop hitting at any time point.  
> 抽牌(hitting)抽到玩家想暫停(staying)或超過21點(bust)

* **specified cards show up:** The number cards (2 through 10) are worth the number displayed, face cards are worth 10, and `ACE` can be worth either **1** or **11**.  
> 如果抽到ACE的話，則考慮當下手中的牌再決定它是成為11或1的點數  
> face cards : JACK, QUEEN, and KING  

* **dealer to 17 points:** Once the player’s hand is finished, the dealer will try to do the same things. The dealer must keep hitting until he gets to 17. 
If the dealer gets above 17 without busting, then they can stay.  
> 換到電腦抽牌時則自動抽到點數大於等於17為止

***

### Finally, the game is settling by simple rules:  
##### (1) if the player has blackjack, he/she wins the game, unless the dealer also has Blackjack, in which case the game is a tie.  
##### (2) If the dealer busts and the player does not, the player wins.  
##### (3) If the player busts, the dealer wins.  
##### (4) If the player and the dealer both do not bust, whoever is closest to 21 wins. 

***
## Getting Started 
The program logic forms the game engine, enforcing the rules of the game.  

**Preprocessing.**  
Create the deck of cards by combing the 13 ranks with 4 suits. Then before the game starts, shuffle the cards.  
```commandline
#create new cards for the specified player 
for i in number:
  for j in card:
    deck.append([i,j])
random.shuffle(deck) #shuffle
```

**Settle the Stage.**  
Send the player’s and dealer’s first two cards by random.  
```commandline
playcard(player,card_num)  #select cards randomly 
```

**Compute the Total Value.** 
Compute the total value of cards in the hand. 
```commandline
def point(cards,pointnum):
  #add the lately gain cards into player's points
...
```


**Game Logic.**  
The program ask the player whether he would like to hit or stay, and continue to ask them until they bust, or he decide to stay. 
Therefore, the program print the player’s cards in the hand and current total value each time before asking for their response and input.
As long as the player’s hand isn’t a bust, we ask for the player’s input: `hit`再抽=1, `stay`停止=0. 
* **hit:** we again deliver him a new card by randomly drawn a card from the remaining cards in the deck, and immediately print the newly drawn card. 
* **stay:** the action of the player will be terminated, and program moves on to the dealer. If the player’s hand isn’t a bust, we print the dealer’s total value and current cards. 
Then, while the dealer’s hand is worth less than 17, the dealer is made to hit. Each time each dealer hits, it prints the new drawn card.
By design, this loop halts when the dealer exceeds 17.  

**Determine the Winner.**  
Compared whose points is closer to 21, then the program prints the winner.


**Ask the Player to play or not.**  
If the player does not want to play again, quit the Blackjack game.  
If the player wants to play again, the program rearrange the deck of cards to let the player play one more time.  
