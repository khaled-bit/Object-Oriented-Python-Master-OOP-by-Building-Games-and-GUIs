import random
from re import L
# suit tuple , rank tuple that will be used in building the dict
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
'Queen', 'King')
#used in the for loop for deciding how many time s to play for the card
NCARDS = 8
#a function to fin the top of the dic
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard
#a function to suffle (change the order) of the dic
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut   

print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()     

#(0,'a') , (1,'b')
startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)
score = 50


while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()


    for cardNumber in range(0, NCARDS):
     answer = input('Will the next card be higher or lower than the ' +currentCardRank + ' of ' +currentCardSuit + '? (enter h or l): ')
     answer = answer.casefold() # force lowercase
     nextCardDict = getCard(gameDeckList)
     nextCardRank = nextCardDict['rank']
     nextCardSuit = nextCardDict['suit']
     nextCardValue = nextCardDict['value']
     print('Next card is:', nextCardRank + ' of ' + nextCardSuit)
     if answer == 'h':
         if nextCardValue > currentCardValue:
          print('You got it right, it was higher')
          score = score + 20
         else:
          print('Sorry, it was not higher')
          score = score - 15
     elif answer == 'l':
         if nextCardValue < currentCardValue:
          score = score + 20
          print('You got it right, it was lower')
         else:
          score = score - 15
          print('Sorry, it was not lower')
          print('Your score is:', score)
          print()
    currentCardRank = nextCardRank
    currentCardValue = nextCardValue # don't need current suit
    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    if goAgain == 'q':break
    